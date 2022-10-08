"""
@author: Nikhil Kumar G

The primary goal of this file is to demonstrate a simple unittest implementation

"""

import unittest

from HomeWork04a import Githubid

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testuserID(self): 
        self.assertEqual(Githubid("nikhil-01a"),'Valid','The User-ID exists')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
