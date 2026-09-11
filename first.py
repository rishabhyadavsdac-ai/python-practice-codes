
# contacts = {}


# def add_contact():
#     name = input("Name: ").strip()
#     if not name:
#         print("Name cannot be empty.")
#         return

#     if name in contacts:
#         print("That contact already exists.")
#         return

#     phone = input("Phone: ").strip()
#     email = input("Email: ").strip()
#     contacts[name] = {"phone": phone, "email": email}
#     print("Contact added.")

# def view_contacts():
#     if not contacts:
#         print("No contacts saved.")
#         return

#     print("\nContacts")
#     for name in sorted(contacts):
#         contact = contacts[name]
#         print(f"- {name}: {contact['phone']} | {contact['email']}")


# def search_contact():
#     search_term = input("Search name: ").strip().lower()
#     matches = [name for name in contacts if search_term in name.lower()]

#     if not matches:
#         print("No matching contacts.")
#         return

#     for name in sorted(matches):
#         contact = contacts[name]
#         print(f"- {name}: {contact['phone']} | {contact['email']}")


# def update_contact():
#     name = input("Name to update: ").strip()
#     if name not in contacts:
#         print("Contact not found.")
#         return

#     phone = input("New phone: ").strip()
#     email = input("New email: ").strip()
#     contacts[name] = {"phone": phone, "email": email}
#     print("Contact updated.")


# def delete_contact():
#     name = input("Name to delete: ").strip()
#     if name not in contacts:
#         print("Contact not found.")
#         return

#     del contacts[name]
#     print("Contact deleted.")


# def main():
#     while True:
#         print("\nContact Book")
#         print("1. Add contact")
#         print("2. View contacts")
#         print("3. Search contact")
#         print("4. Update contact")
#         print("5. Delete contact")
#         print("6. Exit")

#         choice = input("Choose an option: ").strip()
#         if choice == "1":
#             add_contact()
#         elif choice == "2":
#             view_contacts()
#         elif choice == "3":
#             search_contact()
#         elif choice == "4":
#             update_contact()
#         elif choice == "5":
#             delete_contact()
#         elif choice == "6":
#             print("Goodbye!")
#             break
#         else:
#             print("Please choose a number from 1 to 6.")


# if __name__ == "__main__":
#     main()