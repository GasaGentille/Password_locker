from user_account import User
from user_account import Credential

#CREATE
def create_user(username,password):
    '''
    Function to create a new user_account
    '''
    new_user = User(username,password)
    return new_user

def create_credential(credential_name,username,password):
    '''
    Function to create a new credential_account
    '''
    new_credential = Credential(credential_name,username,password)
    return new_credential

#SAVE
def save_user(user):
    
    '''
    Function to save user
    '''
    user.save_user()
    
def save_credential(credential):
    
    '''
    Function to save credential
    '''
    credential.save_credential()
    
    
# DELETE CREDENTIAL

def del_credential(credential):
    '''
    Function to delete credential
    '''
    credential.delete_credential()
    
# FIND CREDENTIAL

def find_credential(password):
    '''
    Function that finds credential by password and returns the credential
    '''
    return Credential.find_by_password(password)
    
def main():
    print("Hello Welcome to your user holder. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new user_account, dc - display contacts, fc -find credential, ex -exit the user list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New User")
                    print("-"*10)

                    print ("Username....")
                    username = input()

                    print("Password ...")
                    password = input()

                    # print("Phone number ...")
                    # p_number = input()

                    # print("Email address ...")
                    # e_address = input()


                    save_user(create_user(username,password)) # create and save new contact.
                    print ('\n')
                    print(f"New User {username} {password} created")
                    print ('\n')

            # elif short_code == 'dc':

            #         if display_contacts():
            #                 print("Here is a list of all your contacts")
            #                 print('\n')

            #                 for contact in display_contacts():
            #                         print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

            #                 print('\n')
            #         else:
            #                 print('\n')
            #                 print("You dont seem to have any contacts saved yet")
            #                 print('\n')

            elif short_code == 'fc':

                    print("Enter the password you want to search for")

                    search_password = input()
                    if check_existing_contacts(search_password):
                            search_password = find_credential(search_password)
                            print(f"{search_credential.username} {search_credential.password}")
                            print('-' * 20)

                            # print(f"Phone number.......{search_contact.phone_number}")
                            # print(f"Email address.......{search_contact.email}")
                    else:
                            print("That credential does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")  
if __name__ == '__main__':

    main()





    