# Google calendar can only handle dates in YYYY-MM-DD format.
# This script looks for DD/MM/YYYY format in a csv and replaces it to YYYY-MM-DD.

# A "contacts.csv" FILE IS EXPECTED IN THE SAME FOLDER AS THE SCRIPT (there will be no edits made to the original file)

import re

with open("contacts.csv", encoding="utf8") as f:
    contacts = f.read().split("\n")

for i, c in enumerate(contacts):
    x = re.findall("[0-9]{2}/[0-9]{2}/[0-9]{4}", c)
    if x:
        if len(x) > 1:
            raise Exception(f"More than one date in contact {i}:\n'{c}'.")
        dd, mm, yyyy = x[0].split("/")
        contacts[i] = re.sub("[0-9]{2}/[0-9]{2}/[0-9]{4}", f"{yyyy}-{mm}-{dd}", contacts[i])

contacts_end = "\n".join(contacts)

with open("contacts-new.csv", "w+", encoding="utf8") as f:
    f.write(contacts_end)