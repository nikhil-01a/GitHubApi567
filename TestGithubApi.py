"""
@author: Nikhil Kumar G

The primary goal of this file is to test the function taking in a github user id and printing the number of repositories and the number of commits in each repository

"""

import unittest

from HomeWork04a import Githubid

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testuserID(self): 
        self.assertEqual(Githubid('nikhil-01a'),'Valid','The User-ID exists')

    def testuserID(self): 
        self.assertEqual(Githubid('a'*(40)),'invalid','The User-ID has more than 39 characters')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
 