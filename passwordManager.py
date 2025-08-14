import hashlib



print("PASSWORD MANAGER\n")

usernameStorage = dict()

# Loop for menu options
while True:
    print("------------Menu Options------------\n")

    print("To enter and store a password type 1.\n")
    print("To Login type 2.\n")
    print("Quit password manager type 3.\n")

    # User path for login, password, and quit
    userPath = input("What would you like to do? (1, 2, 3): ")

    # Option 1: Add username and password
    if userPath == "1":
        userPathPassword = input("Would you like to store a password? Yes/No: ")
        
        # Confirming if the user wants to enter a password
        if userPathPassword.lower() == "yes":
            newUsername = input("Enter a username: ")
            newUserPassword = input("Enter a password: ")

            hashedPassword = hashlib.sha256(newUserPassword.encode()).hexdigest()

            if newUsername not in usernameStorage:
                usernameStorage[newUsername] = hashedPassword
                print(f"User '{newUsername}' has been added.")
            else:
                print(f"Username '{newUsername}' already exists.")

        elif userPathPassword.lower() == "no":
            print("Returning to the main menu.")

        else:
            print(f"'{userPathPassword}' is not a valid option.")

    # Option 2: Login
    elif userPath == "2":
        loginUser = input("Enter login username: ")
        loginPass = input("Enter login password: ")

        if loginUser in usernameStorage:
            # Hash the entered password and compare with the stored one
            hashedLoginPass = hashlib.sha256(loginPass.encode()).hexdigest()

            if usernameStorage[loginUser] == hashedLoginPass:
                print("Login successful!")
                # Loop for logged-in user options
                while True:
                    print("------------User Options------------\n")
                    print("To change password type 1.\n")
                    print("To logout type 2.\n")

                    userOption = input("What would you like to do? (1, 2): ")

                    if userOption == "1":
                        newPassword = input("Enter a new password: ")
                        newHashedPassword = hashlib.sha256(newPassword.encode()).hexdigest()
                        usernameStorage[loginUser] = newHashedPassword
                        print("Password updated successfully.")

                    elif userOption == "2":
                        print("Logging out...")
                        break  # Exit the logged-in user's loop

                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please try again.")

    # Option 3: Quit
    elif userPath == "3":
        print("Quitting password manager.")
        break  # This will quit the entire program

    else:
        print("Please enter a valid option.")

            

        
