import json
import os
import re


#defining Contact class
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"Name:{self.name}\nPhone Number:{self.phone}\nEmail:{self.email}"
    

#functions
class contactsFunction:
    def __init__(self,folder="week1-tasks",filename="contacts.json"):
        self.filename=filename
        self.contacts = self.contactsFile()

    #load json file
    def contactsFile(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                try:
                    contactsList=json.load(file)
                    return{name:Contact(**details) for name,details in contactsList.items()}
                except json.JSONDecodeError:
                    print("Error: The file does not contain valid JSON.")
                    return {}
        return {}
        

    #save contact
    def saveContacts(self):
        with open(self.filename,'w')as file:
            contactsList = {name:contact.__dict__ for name,contact in self.contacts.items()} 
            json.dump(contactsList,file,indent=4)


    #validation (name,email and phone number)
    def validateName(self,name):
        pattern=r'^[a-zA-Z]+$'
        return re.match(pattern,name) is not None
    def validateEmail(self,email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    def validatePhoneno(self,phone):
        pattern = r'^\d{10}$'
        return re.match(pattern, phone) is not None
    
    
    # contacts
    def showContacts(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                contactsList=json.load(file)
                for name, details in contactsList.items():
                        contact = Contact(**details)
                        print(contact)
        
        
    #adding contact function
    def addContacts(self,name,phone,email):
        if not self.validateName(name):
            print("Please enter alaphabets only in Name!")
            return
        if not self.validateEmail(email):
            print("Invalid email format!")
            return
        if not self.validatePhoneno(phone):
            print("Invalid phone number! It should be 10 digits only")
            return
        if name in self.contacts:
            print("Contact already exits!!")
            return
        self.contacts[name]=Contact(name,phone,email)
        self.saveContacts()
        print("Contact added successfully")

    #search function
    def searchContact(self, name):
        status = False
        searchName = name.lower()
        print(f"Searching for: {searchName}")
        for contactName in self.contacts:
            if searchName in contactName.lower():
                print(self.contacts[contactName])
                status = True
        if not status:
            print(f"Contact {name} not found!!")
    
                
    #update function
    def updateContact(self,name,phone,email):
        if not self.validateEmail(email):
            print("Invalid email format!")
            return
        if not self.validatePhoneno(phone):
            print("Invalid phone number! It should be 10 digits")
            return
        if name in self.contacts:
            self.contacts[name].phone = phone
            self.contacts[name].email = email 
            self.saveContacts()
            print("Updated successfully") 
        else:
            print("Contact not found!!")

    #delete function
    def deleteContact(self,name):
        if name in self.contacts:
            status=input(f"Are you sure You want to delete the contact '{name}' ? (Yes/No):").strip().lower()
            if status=='yes':
                del self.contacts[name]
                self.saveContacts()
                print("Deleted successfully")
            else:
                print("Deletion cancelled!!")
        else:
            print("Contact not found")


# command line interface function
def main():
    cms=contactsFunction('contacts.json')

    while True:
        print("\nContact Management System")
        print("\n1. Contacts")
        print("\n2. Add Contact")
        print("\n3. Search Contact")
        print("\n4. Update Contact")
        print("\n5. Delete Contact")
        print("\n6. Exit")
        choice=input("\nEnter your choice: ").strip()

        if choice =='1':
            cms.showContacts()
        elif choice=='2':
            name=input("Enter name: ").strip()
            phone=input("Enter phone number: ").strip()
            email=input("Enter email: ").strip()
            cms.addContacts(name,phone,email)
        elif choice=='3':
            name=input("Enter name: ").strip()
            cms.searchContact(name)
        elif choice=='4':
            name=input("Enter name to update: ").strip()
            phone=input("Enter  new phone number: ").strip()
            email=input("Enter  new email: ").strip()
            cms.updateContact(name,phone,email)
        elif choice=='5':
            name=input("Enter name to delete: ").strip()
            cms.deleteContact(name)
        elif choice=='6':
            print("Exiting CMS, Goodbye!")
            break
        else:
            print("Invalid choice!try again")

if __name__=="__main__":
    main()
            


      


        

                  
