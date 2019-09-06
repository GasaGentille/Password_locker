class User:
    """
    Class that generates new instances of user account
    """
    user_holder =[]

    def __init__(self,username,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_username: New user username.
            user_password: New user password.
        '''
        self.user_username = username
        self.user_password = password
    def save_user(self):
        '''
        save_user method saves user objects into user_holder
        '''
        User.user_holder.append(self)

class Credential:
    """
    Class that generates new instances of credential accounts
    """
    credential_holder =[]

    def __init__(self,credential_name,username,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            social_media = New credential credential_name
            credential_username: New credential username.
            credential_password : New credential password.
        '''
        self.social_media= credential_name
        self.credential_username =username
        self.credential_password = password
    def save_credential(self):
        
        '''
        save_credential method saves credential objects into credential_holder
        '''
       Credential.credential_holder.append(self)