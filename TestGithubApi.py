"""
@author: Nikhil Kumar G
The primary goal of this file is to test the function taking in a github user id and printing
the number of repositories and the number of commits in each repository.

"""

import json
import unittest
from unittest import mock
from HomeWork04a import Githubid


class MockResponse:
    def __init__(self,json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

    status_code=200

def mocked_requests_get(*args):
    if args[0] in switcher:
        with open(switcher[args[0]], encoding="utf-8") as f:
            return MockResponse(json.load(f))
    return MockResponse(None)

switcher = {
    'https://api.github.com/users/nikhil-01a/repos' : 'resources/nikhil-01a_repos.json',
    'https://api.github.com/repos/nikhil-01a/GitHubApi567/commits' : 'resources/GitHub567_commitcount.json',
    'https://api.github.com/repos/nikhil-01a/Triangle567/commits' : 'resources/Triangle567_commits.json',
    'https://api.github.com/repos/nikhil-01a/TrianglePylint/commits' : 'resources/TrianglePylint_commits.json',
}

class TestGithubApi(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    @mock.patch('requests.get', side_effect = mocked_requests_get)
    def testuserID(self, mock_get): 
        self.assertEqual(Githubid('nikhil-01a'),'Valid','The User-ID exists')
        if mock_get:
            print("Used the mock object")

    def testuserID_valid(self): 
        self.assertEqual(Githubid('a'*(40)),'Username invalid','The User-ID has more than 39 characters')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
 