source .venv/bin/activate

if [ ! -z "$1" ]
then
    python -m pdb venmo_email_fetch.py -c "b ${1}" -c "c" 
else
    python -m pdb venmo_email_fetch.py -c c
fi

deactivate
