import os
from datetime import datetime
from dotenv import dotenv_values 
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# --- Configuration ---
config = dotenv_values()
SCOPES = config.get("SCOPES")
TOKEN_PATH = config.get("TOKEN_PATH")
CREDENTIALS_PATH = config.get("CREDENTIALS_PATH ")
LABEL_NAME = config.get("LABEL_NAME")
	
def authenticate_gmail():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def get_label_id(service, label_name):
    labels = service.users().labels().list(userId='me').execute().get('labels', [])
    for label in labels:
        if label['name'] == label_name:
            return label['id']
    raise ValueError(f"Label '{label_name}' not found.")

def get_unread_emails(service, label_id):
    response = service.users().messages().list(
        userId='me',
        labelIds=[label_id, 'UNREAD']
    ).execute()
    return response.get('messages', [])

def get_message(service, msg_id): return service.users().messages().get(userId='me', id=msg_id, format='minimal').execute()
def get_snippet(msg): return msg['snippet']
def get_date(msg): return datetime.fromtimestamp(msg['internalDate'])

def get_snippet_details(snippet):     
    def get_money_from_str(string):
        amount = ""
        split_substr = ""
        for c in string:
            if c in " ":
                split_substr += c
            elif c in "$0123456789.":
                amount += c
                split_substr += c
            else:
                break
        _empty, rest = string.split(split_substr, 1)
        return amount, rest

    msg = ""

    # transfer from Venmo balance to bank account
    if "issued your transfer" in snippet:
        _, msg = snippet.split("Initiated on ")
        _, msg = msg.split("Transfer Amount")
        amt, msg = get_money_from_str(msg)
        est_date = msg.split("Estimated arrival")[1]
        return {
            "type": "transfer",
            "amount": amt.strip(),
            "est_date": est_date.strip(),
        }

    else: # actual Venmo transaction
        # requested or sent unprompted by user
        if re.match("You paid", snippet):
            requester, msg = snippet[8:].split('$', 1)
            amt, msg = get_money_from_str(msg)

        # requested or sent unprompted by other party
        elif "paid you" in snippet:
            requester, msg = snippet.split("paid you", 1)
            amt, msg = get_money_from_str(msg)

        else: # not an email for us to parse
            return

        # payment sent by user
        if re.match("You paid", msg):
            payer = "_SELF_"
            payee, msg = msg[8:].split('$', 1)
        
        # payment sent to user
        else:
            payee = "_SELF_"
            payer, msg = re.split("paid you", msg, maxsplit=1, flags=re.IGNORECASE)
            # payer, msg = snippet.split("paid you", 1)

        _, msg = get_money_from_str(msg)
        comment = ""
        if "See transaction" in msg:
            comment, msg = msg.split("See transaction", 1)
        method = ""
        if "Payment Method" in msg:
            msg = msg.split("Payment Method")[1]
            method = msg.split("Sent")[0] if "Sent" in msg else msg
        return {
            "type": "payment",
            "requester": requester.strip(),
            "payer": payer.strip(),
            "payee": payee.strip(),
            "amount": amt.strip("$ "),
            "notes": comment.strip(),
            "method": method.strip()
        }

def mark_as_read(service, msg_id):
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()

def main():
    service = authenticate_gmail()
    label_id = get_label_id(service, LABEL_NAME)
    unread_msgs = get_unread_emails(service, label_id)
    transactions = []

    if not unread_msgs:
        return
    else:
        for message in unread_msgs:
            msg_id = message['id']
            msg_info = get_message(service, msg_id)
            snippet = get_snippet(msg_info)
            details = get_snippet_details(snippet)
            details['date'] = datetime.fromtimestamp(int(msg_info['internalDate'])/1000.0).isoformat()
            # with open('fetch_venmo.log', 'a') as f:
            #     f.write(str(details)+'\n')
            transactions.append(details)
            mark_as_read(service, msg_id)
    return transactions

def log_results():
    LOG_FILE = config.get("LOG_PATH")
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        info = main()
        f.write(f"{datetime.now().strftime('%m-%d-%Y %H:%M:%S')} | {'No unread emails.' if not info else 'New transactions found: '}")
        if info:
            for transaction in info:
                f.write("\n\t" + str(transaction)) 
        f.write("\n")   

if __name__ == "__main__":
    log_results()
