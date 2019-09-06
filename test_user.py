import unittest
from user_account import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user_account = User("GasaGentille","555a")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user_account.user_username ,"GasaGentille" )
        self.assertEqual(self.new_user_account.user_password ,"555a" )
        
        #SAVING OUR LOGIN DETAILS
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user_holder
        ''' 
        self.new_user_account.save_user()
        self.assertEqual(len(User.user_holder),1)
    


if __name__ == '__main__':
    unittest.main()