# import unittest
# from user_account import Credential

# class TestCredintial(unittest.TestCase):
#     '''
#     Test class that defines test cases for the Credential class behaviours.

#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''
#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_credential_account = Credential("twitter","GasaGentille","555a")

#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properly
#         '''
#         self.assertEqual(self.new_user_account.user_username ,"GasaGentille" )
#         self.assertEqual(self.new_user_account.user_password ,"555a" )

#     def tearDown(self):
#             '''
#             tearDown method that does clean up after each test case has run.
#             '''
#             User.user_holder = []
        
#         #SAVING OUR LOGIN DETAILS
#     def test_save_user(self):
#         '''
#         test_save_user test case to test if the user object is saved into
#          the user_holder
#         ''' 
#         self.new_user_account.save_user()
#         self.assertEqual(len(User.user_holder),1)
        
#         #SAVING MULTIPLE LOGIN DETAILS
#     def test_save_multiple_user(self):
#         '''
#         test_save_multiple_user to check if we can save multiple user
#         objects to our user_holder
#         '''  
#         self.new_user_account.save_user()
#         test_user = User("rita","kaka1")
#         test_user.save_user()
#         self.assertEqual(len(User.user_holder),2)



if __name__ == '__main__':
    unittest.main()