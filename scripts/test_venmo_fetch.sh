if [ ! -z "$1" ]
then
    python -m pdb src/venmo_email_fetch.py -c "b ${1}" -c "c" 
else
    python -m pdb src/venmo_email_fetch.py -c c
fi
