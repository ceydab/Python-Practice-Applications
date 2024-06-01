'''
this project is an example of api utilization. the project accesses github api and obtains user or 
repository information.
'''

import requests


class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"

    def getUser(self, username):
        response = requests.get(self.api_url+ "/users/" + username)
        return response.json()
        
    def getRepositories(self, username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()



github = Github()
while True:
    select = input("1- User\n2- Get repository\n3- Exit\nSelect:")

    if select == "4":
        break
    else:
        if select == "1":
            username = input("username: ")
            result = github.getUser(username)
            print(result)

        elif select == "2":
            username = input("username: ")
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])

        else:
            print("Select again.")
