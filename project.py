Contacts = {
    "Adarsh Singh": "9555589871",
    "Harsh Singh": "8083298887",
    "Vanshraj Rohilla": "9457360397",
    "Diptesh Kumar": "9337393440",
    "Arshdeep": "8492916021",
    "Aditya Chaturvedi": "5678901234",
    "Ayush Srivastava": "6789012345",
    "Shubham Singh": "7890123456",
    "Sujal Chauhan": "8901234567",
    "Jayant Kumar": "9012345678",
    "Shivam Kumar": "6207920403",
    "Sagar Bisht": "1234567890",
    "Jai": "2345678901",
    "Abhishek": "9813801061",
    "Himanshu": "7457964922"
}
def display_Contacts():
    print("Name\t\tContact Number")
    for key in Contacts:
        print("{}\t\t{}".format(key,Contacts.get(key)))

while True:
    choice = int(input("Enter your Choice \n 1. Search Contacts \n 2. Display all Contacts with names \n 3. Search Multiple Contacts one by one \n 4. Exit\n"))
    if True and choice == 1:
        name = input("Enter the student's name_ \n  ")
        if name in Contacts:
            print(" \n ",name,"'s contact number is",Contacts[name]," \n ")
        else:
            print("Name is not found in contact book \n ")
    elif choice == 2:
        display_Contacts()
    elif choice == 3:
        while True:
            name = input("Enter the student's name_ \n  ")
            if name in Contacts:
                print(" \n ",name,"'s contact number is",Contacts[name]," \n ")
                print(" \n Enter another student's name or Enter 0 to exit to main menu \n") 
            else:
                print("Name was not found in contact book \n ")
                break
    elif choice == 4:
        break
    else:
        print(" \n Please choose a valid option \n ")