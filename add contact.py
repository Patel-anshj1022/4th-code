# Define an empty contacts dictionary
contacts = {}

# Function to add a new contact
def add_contact(name, phone, email):
    # Add the contact details to the contacts dictionary
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully!\n")

# Function to display all contacts
def display_contacts():
    if contacts:
        print("Contacts List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print("No contacts found!\n")

# Example usage
add_contact("John Doe", "123-456-7890", "john.doe@example.com")
add_contact("Jane Smith", "987-654-3210", "jane.smith@example.com")

# Display the updated list of contacts
display_contacts()
