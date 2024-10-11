import json
import os

filename = "passwords.json"
password_saved = "passwordtotal.json"

if os.path.exists(password_saved):
    with open(password_saved, "r") as ps:
        passkey = json.load(ps)
        enter_pass = input("Enter your password: ")
        if enter_pass == passkey:
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    my_dict = json.load(file)
            else:
                my_dict = {}

            while True:
                decision = input("Would you like to add/delete or see currently added passwords? Add/See/Delete/Exit: ").lower()

                if decision == "add":
                    username_email = input("Enter your username/email: ")
                    password = input("Enter your password: ")
                    my_dict[username_email] = password

                    with open(filename, "w") as file:
                        json.dump(my_dict, file)
                        print("Password added successfully!")

                elif decision == "see":
                    search_key = input("Enter the email/username you would like to see the password for: ")
                    if search_key in my_dict:
                        print(f"The password for '{search_key}' is: {my_dict[search_key]}")
                    else:
                        print(f"Username/Email '{search_key}' not found in the dictionary.")

                elif decision == "delete":
                    search_key = input("Enter the username/email you would like to delete: ")
                    if search_key in my_dict:
                        removed_value = my_dict.pop(search_key)
                        print(f"Removed Key '{search_key}' with value: {removed_value}")

                        with open(filename, "w") as file:
                            json.dump(my_dict, file)
                            print("Password deleted successfully!")
                    else:
                        print(f"Username/Email '{search_key}' not found in the dictionary.")

                elif decision == "exit":
                    print("Exiting the password manager.")
                    break  

                else:
                    print("Invalid option. Please choose Add, See, Delete, or Exit.")

        else:
            print("Incorrect password. Access denied.")  
else:
    inputing_pass = input("Create a passkey to continue: ")
    with open(password_saved, "w") as ps:
        json.dump(inputing_pass, ps)
        print("Passkey created successfully!")
