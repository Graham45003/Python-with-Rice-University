def lookup2(contacts, name):
    """
    Lookup name in contacts and return phone number.
    If name is not in contacts, return an empty string.
    """
    return contacts.get(name, "contact does not exist")

def print_contact_list(contacts):
    """
    Print the names and phone numbers of the contacts in
    our contacts list.
    """
    for name, number in contacts.items():
        print(name, ":", number)
        
def print_ordered(contacts):
    """
    Print the names and phone numbers of the contacts
    in our contacts list in alphabetical order.
    """
    keys = contacts.keys()
    names = sorted(keys)
    for name in names:
        print(name, ":", contacts[name])
        
def add_or_update_contact(contacts, name, number):
    """
    Add contact or update it if it is already in the contacts list.
    """
    contacts[name] = number
    
def add_or_update2(contacts2, last, details):
    contacts2[last] = details