"""
@author: Nikhil Kumar G
Program: This program is used to take a 'github user id' as an input from the user and give the name of the repository and the number of commits in those repositories as output.

"""
#importing modules

import requests

#Main function to retrieve and return the name of the repositories
def Githubid(username):

    #Adding one of the Github username rule for tester to check if the username is not exceeding 39 characters
    temp = list(username)
    if len(temp) > 39:
        return 'Username invalid'

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

    #Added a status check verification so that the tester can use its return value and test the availability of user-id
    check = response.status_code 
    if (check == 200):
        return 'Valid'

if __name__ == '__main__':
    uid = input('Enter your github user id: ')
    Githubid(uid)                                    #Calling main function