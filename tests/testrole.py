import unittest

from app.models import Role



class Role(unittest.TestCase):

    '''

    Test Class to test the behaviour of the Writer class

    '''

    def setUp(self):

        '''

        test to run before each tests

        '''

        self.new_role = role(username = 'karimikim',password = 'banana', email = 'karimikim3@gmail.com')



    def test_password_setter(self):

        self.assertTrue(self.new_writer.password_secure is not None)



    def test_no_access_password(self):

        with self.assertRaises(AttributeError):

            self.new_writer.password



    def test_password_verification(self):

        self.assertTrue(self.new_writer.verify_password('banana'))



    def tearDown(self):

        Writer.query.delete()