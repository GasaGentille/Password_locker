# lt = list()
# # a = [1, 2]
# # b = [3, 4]
# # c = [5, 6]
# # c = [7, 8]
# # lt.append(a)
# # lt.append(b)
# # lt.append(c)
# # tl = []
# # for i in range(10):
# #     tl.append(i)
# #     lt.append(tl)

# # print(lt)
# # print("\n")
# # print(lt[1])


# import os
# class User:
#     """
#     Class that generates new instances of user account
#     """
#     user_holder =[]

#     def __init__(self,username,password):
#         '''
#         __init__ method that helps us define properties for our objects.

#         Args:
#             user_username: New user username.
#             user_password: New user password.
#         '''
#         self.user_username = username
#         self.user_password = password
#         self.save_user(self.user_username, self.user_password)
#     def save_user(self, usrname, pwd):
#         '''
#         save_user method saves user objects into user_holder
#         '''
#         list1 = []
#         list1.append(usrname)
#         list1.append(pwd)
#         User.user_holder.append(list1)
#         # User.user_holder.append(usrname)
#         # User.user_holder.append(pwd)
#         return self.user_holder
    
# while True:
#     print("Enter credentials\n")
#     uname = input("username: \n")
#     pwd = input("password: \n")
#     n_user = User(uname, pwd)
#     print(n_user.user_holder)

# from random import randint

# first_Args = 123
# second_Args = "abc"
# # tt_Args = 
# times = input("How many caracters do you want for your password?\n")

# pswrd = randint(3, first_Args);
# print(pswrd)

# import pyperclip
# import random
# import string

# # string = "nkhk"
import string
import random
def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

pdd = generate_password();
print(pdd)


# def delete_credential():
#     pass

# acc = "facebook"
# uname = "gentille"
# pwd = "123"

# acc2 = "twitter"
# uname2 = "gasa"
# pwd2 = "456"

# arr = []
# arr.append(uname)
# arr.append(pwd)

# arr2 = []
# arr2.append(uname2)
# arr2.append(pwd2)

# dic = dict()
# dic.update([(acc, arr)])
# dic.update([(acc2, arr2)])
# print(dic)

# def delete_credential():
#     holedkey = ""
#     cle = input("enter credential account name to be deleted\n")
#     for key in dic.keys():
#         if(key == cle):
#             # del dic[key]
#             holedkey = key
#     del dic[holedkey]
#     print(dic)
# delete_credential()


# @classmethod
# def find_by_site_name(cls, site_name):
#     '''
#     Method that takes in a site_name and returns a credential that matches that site_name.
#     '''
#     for credential in cls.credential_holder:
#         if credential.keys() == site_name:
#             return credential

# @classmethod
# def copy_credential(cls,site_name):
#     '''
#     Class method that copies a credential's info after the credential's site name is entered
#     '''
#     find_credential = Credential.find_by_site_name(site_name)
#     return pyperclip.copy(cls.credential_holder[site_name])
