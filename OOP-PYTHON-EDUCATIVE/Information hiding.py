# ENCAPSULATION
class User():
    def __init__(self, username=None):
        self.__username = username #private
    def setUsername(self, x):
        self.__username = x
    def getUsername(self,):
        return self.__username

user1 = User('Steve1')
y =user1.setUsername('Steves Username')
print(user1.getUsername())

class User():

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if(self.__username.lower() == username.lower() and (self.__password == password)):
            print("Access granted")
        else:
            print('Invaid')


Steve = User("Steve", "12345") ##created a new User object and stored the password and username
Steve.login("steve", "12345") # Grants access because credentials are valid
Steve.login("steve", "6789") # does not grant access since the credentails are invalid
 # Steve.__password # compilation error will occur due to this line