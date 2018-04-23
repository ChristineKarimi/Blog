import unittest

from app.models import Blog



class BlogModelTest(unittest.TestCase):

    '''

    Test Class to test the behaviour of the Blog class

    '''



    def setUp(self):

        '''

        test to run before each tests

        '''

        self.blogs= Blog(title = 'straightup', blog = 'straight up and down')





    def tearDown(self):

        Blog.query.delete()



    def test_instance(self):

        self.assertTrue(isinstance(self.blogs, Blog))



    def test_check_instance_variables(self):



        self.assertEquals(self.blogs.title,'straightup')

        self.assertEquals(self.blogs.blog,'straight up and down')





    def test_save_blog(self):

        self.blogs.save_blog()

        self.assertTrue(len(Blog.query.all())>0)