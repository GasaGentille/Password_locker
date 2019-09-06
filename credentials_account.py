# class Credential:
#     """
#     Class that generates new instances of credential accounts
#     """
#     Credential_holder =[]

#     def __init__(self,credential_name,username,password):
#         '''
#         __init__ method that helps us define properties for our objects.

#         Args:
#             credential_name: New user username.
#             user_password: New user password.
#         '''
#         self.social_media= username
#         self.credential_username =username
#         self.credential_password = password
#     def save_user(self):
#         '''
#         save_user method saves user objects into user_holder
#         '''
#         User.user_holder.append(self)