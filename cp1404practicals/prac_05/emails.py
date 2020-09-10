"""
CP1404 Practical 05
emails
"""

email = input("Email: ")
email_book = {}
while email != "":
    temp_name = email.split("@")[0]  # splits email at "@" and takes the first part
    temp_name = temp_name.split(".")
    persons_name = ""
    for name in temp_name:
        persons_name += name.title() + " "
    try:
        name_change = input("Is your name {}? (Y/n) ".format(persons_name))
        if name_change[0] in "Nn":
            persons_name = input("Name: ")
    except IndexError:
        no = 1  # Awful placeholder as I'm out of ideas.
    email_book[persons_name] = email
    email = input("Email: ")
for entry in email_book:
    print("{}({})".format(entry, email_book[entry]))