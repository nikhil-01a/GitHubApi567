"""
@author: Nikhil Kumar G
Program: This program is used to take a 'github user id' as an input from the user and give the name of the repository and the number of commits in those repositories as output.

"""
#importing modules
import json
import requests

#uid = input('Enter your github user id: ')

#Main function to retrieve and return the name of the repositories
def Githubid(username):

    #seperate function to retrieve and return the number of commits (I have it inside main function so that it need not be tested seperately)
    def countcommits(username,repo):
        urlc = "https://api.github.com/repos/%s/%s/commits"% (username,repo)
        commit_count = requests.get(urlc).json()
        count = len(commit_count)
        return count

    url = "https://api.github.com/users/%s/repos"%username
    repo_name = requests.get(url).json()
    
    for project in repo_name:    
        repo = f"{project['name']}"
        print(f"Repo: {repo}, Number of Commits: {countcommits(username,repo)}")

    response = requests.get(url)
    check = response.status_code #Added a status check verification so that the tester can use its return value and test the availability of user-id
    if (check == 200):
        return 'Valid'

#Calling main function  
#Githubid(uid)