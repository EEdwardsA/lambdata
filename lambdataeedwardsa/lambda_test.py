"""Basic unit test for lambdata package"""

import unittest

import pandas as pd

from example_module import colors, increment
from oop_example import SocialMediaUser
from random import randint
from assignment_module import wrangle_df

df = pd.read_csv('../data/ramen-ratings.csv')
target = 'Top Ten'

class DFCleanerTests(unittest.TestCase):
    """Testing the df_cleaner function"""

    def test_X_size(self):
        """Test that X_train plus X_test are equal in size to X"""
        output = wrangle_df(df)
        self.assertEqual(output[2].shape[0] + output[3].shape[0], output[0].shape[0])
    
    def test_y_size(self):
        """Test that y_train plus y_test are equal in size to y"""
        output = wrangle_df(df)
        self.assertEqual(output[4].__len__() + output[5].__len__(), output[1].__len__())


# class SocialMediaUserTests(unittest.TestCase):
#     """Tests for the usage of social media users in our social media class"""
#     def setUp(self):
#         self.user1 = SocialMediaUser(name='Jimmy', location='France')
#         self.user2 = SocialMediaUser(name='Greg', location='Kenya')
#         self.user3 = SocialMediaUser(name='Nicky', location='Genoa')

#     def test_name(self):
#         """test the name attribute"""
#         self.assertEqual(self.user1.name, 'Jimmy')
#         self.assertEqual(self.user2.name, 'Greg')

#     def test_location(self):
#         """testing the location attribute"""
#         self.assertEqual(self.user1.location, 'France')
#         self.assertEqual(self.user2.location, 'Kenya')

#     def test_default_upvotes(self):
#         """testing default upvotes"""
#         self.assertEqual(self.user3.upvotes, 0)

#     def test_unpopular(self):
#         """testing if is_popular method works"""
#         self.assertFalse(self.user3.is_popular())
#         self.user3.receive_upvotes(randint(101,10000))
#         self.assertTrue(self.user3.is_popular())


# class ExampleTests(unittest.TestCase):
#     """making sure examples work as expected"""
#     def test_increment(self):
#         """Testing that increment function adds 1 to a number"""
#         x0 = 0
#         y0 = increment(x0)
#         self.assertEqual(y0, 1)

#         x1 = 100
#         y1 = increment(x1)
#         self.assertEqual(y1, 101)

#         x2 = -1
#         y2 = increment(x2)
#         self.assertEqual(y2, 0)

#         x3 = -1.5
#         y3 = increment(x3)
#         self.assertEqual(y3, -0.5)

#     def test_colors(self):
#         """testing the presence/absence of colors in the colors list"""
#         self.assertIn('crimson', colors)
#         self.assertNotIn('yellow', colors)

#     def test_len_colors(self):
#         """testing the number of colors in the colors list"""
#         self.assertEqual(len(colors), 4)

if __name__ == "__main__":
    unittest.main()








