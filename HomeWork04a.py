import json
import requests

def Githubid():
    username = input('Enter your github user id: ')
    url = "https://api.github.com/users/%s/repos"%username
    

    #print(url)
    repo_name = requests.get(url).json()

    for project in repo_name:
        repo = f"{project['name']}"
        urlc = "https://api.github.com/repos/%s/%s/commits"% (username,repo)
        print(f"Repo: {project['name']} Number of Commits: {len(urlc)}")
    #print(user_data)
    #print('Repo: %s Number of commits: %s')
    
Githubid()

