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
