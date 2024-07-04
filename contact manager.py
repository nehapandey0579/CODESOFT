class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts:
            if search_term in [contact.name, contact.phone]:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                found = True
                break
        if not found:
            print("Contact not found!")

    def update_contact(self):
        search_term = input("Enter name or phone number to update: ")
        found = False
        for contact in self.contacts:
            if search_term in [contact.name, contact.phone]:
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone number: ")
                contact.email = input("Enter new email: ")
                contact.address = input("Enter new address: ")
                print("Contact updated successfully!")
                found = True
                breakc
        if not found:
            print("Contact not found!")  

    def delete_contact(self):
        search_term = input("Enter name or phone number to delete: ")
        found = False
        for contact in self.contacts:
            if search_term in [contact.name, contact.phone]:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break
        if not found:
            print("Contact not found!")

def main():
    contact_manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            contact_manager.add_contact()
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.search_contact()
        elif choice == "4":
            contact_manager.update_contact()
        elif choice == "5":
            contact_manager.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()