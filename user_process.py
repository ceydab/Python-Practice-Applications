'''this project is an example of user creation and login logout processes. 
the project creates a class User to obtain user information and uses 
class UserRepository to store user data and registration&login information.
In the end, it runs a loop to ask the user what s/he would like to do.
'''

import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetofile()
        print("User created.\n")

    def login(self, username, password):
            
            for user in self.users:
                if user.username == username and user.password ==password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print('Log in successful')
                    break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Log out successful.")
        
    def identity(self):
        if self.isLoggedIn :
            print(f"username: {self.currentUser.username}")
        else:
            print("No logged in user.")
    def savetofile(self):
        list1 = []

        for user in self.users:
            list1.append(json.dumps(user.__dict__))

        with open("users.json", 'w') as file:
            json.dump(list1, file)


repository = UserRepository()
while True:
    print("Menu".center(50, " "))
    select = input("1- Sign up\n2- Sign in\n3- Sign out\n4- Identity\n5- Exit:\n")
    if select == '5':
        break
    else:
        if select =='1':
            username = input("Username: ")
            password = input("Password: ")
            email = input("E-mail: ")

            user = User(username = username, password = password, email = email)
            repository.register(user)
            #print(repository.users)    

        elif select == '2':
            if repository.isLoggedIn:
                print("Already logged in!")
            else:
                username = input("Username: ")
                password = input("Password: ")
                repository.login(username, password)

        elif select == '3':
            repository.logout()
        elif select == '4':
            repository.identity()
