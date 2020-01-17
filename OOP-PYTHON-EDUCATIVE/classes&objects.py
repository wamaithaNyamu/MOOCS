# in python a class is defined as
class ClassName:
    pass

# creating a class object
class MyClass:
      pass

    # creating a class object
obj=MyClass()

# class implementation
# class can be implemented in two ways
# initilising the class varibles when a class is defined or wihin the main function

# 1. Initialising the varibles in the main function
class Employee:
    # employee attributes initalized to none. Without initalisation the code will not run
    ID: None
    salary = None
    dept = None

# create an object of the class
# a class is initialised just like we do when calling a func. Python can tell the diff between a class intialisation and a func call

Steve = Employee()

Steve.ID = 124455
Steve.salary = 22345
Steve.dept = "HR"

# 2 initialising on function declaration
class Employee:
    # defining the properties and assigning values to them
    ID = 3789
    salary = 2500
    department = "Human Resources"


# cerating an object of the Employee class

# creating new attributes for steve that are not in the class
Steve.title = "manager"
# INITIALISER--------------------------------------------------------------
class Employee:
    # the initialiser class has underscores to mark it is as a spcial func and accepts self as its default arg

    def __init__(self, ID, salary, dpt):
        self.ID = ID
        self.salary = salary
        self.dpt =dpt
John = Employee(123,2345,"HR")
# INITIALISER WITH OPTIONAL PARAMS
class Employee:
    # defining the properties and assigning None to them
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
Steve = Employee()
Mark = Employee("3789", 2500, "Human Resources")
# INSTANCE VARIABLES AND CLASS VAIRABLES
# class variables are instantiated in all the class instances while instance var are only applied to the specific instance
class Player:
    # class variables
    team = 'Liverpool'

    def __init__(self, name):
        # instance variable
        self.name = name;

p1 = Player('Mark')
p2 = Player('Ken')
# METHODS IN A CLASS-------------------------------------------------
class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# initializing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")

# METHOD OVERLOADING...............................
class Employee:
    def __init__(self, ID=None, Salary=None, dpt=None):
        self.ID =ID
        self.Salary = Salary
        self.dpt= dpt

        # method overload
    def demo(self, a,b,c,d=5, e=None):
        print("a is" , a)
        print("b is" , b)
        print("c is" , c)
        print("d is" , d)
        print("e is" , e)

    def tax(self, title = None):
        return(self.Salary * 0.2)

    def salaryPerDay(self):
        return (self.Salary / 30)

Steve = Employee(123,1234567,'Finance')


# Printing properties of Steve
# print ("Demo 1")
# Steve.demo(1, 2, 3);
# print("\n")
#
# print ("Demo 2")
# Steve.demo(1, 2, 3, 4);
# print("\n")
#
# print ("Demo 3")
# Steve.demo(1, 2, 3, 4, 5);

# CLASS METHODS AND STATIC METHODS--------------------------------------------
# there are three types of methods, instance methods class ethods and static methods
# CLASS METHODS
class MyClass:
    classVariable = 'Educative'

    @classmethod
    def demo(cls):
        return cls.classVariable



class Player:
    team = 'Liverpool'
    def __init__(self, name):
        self.name = name

    @classmethod
    def getTeamName(cls):
       return  cls.team

Alex = Player('alex')

# print(Alex.name)
# print(Alex.getTeamName())
#


# STATIC METHODS
class Player:
    team = 'Liverpool'

    def __init__(self, name):
        self.name = name

    @staticmethod

    def demo():
        print('Static method')


x =Player('Alex')
x.demo()
Player.demo()
#ACCESS MODIFIERS
# access restrictions are imposed using access modifiers
# they are tags that determine which part of the program can be accessed directly
# PRIVATE ATTRIBUTES
class MyClass:
    def __init__(self, salary):
        self.__salary = salary #private attribute that cant be accessed outside the class

# print(MyClass.__salary)  this throws an error
# PRIVATE METHODS
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary()
# Steve.__displayID()  # this will generate an error

# when its extremely necessary to access private property or method we use the _<classname> prefix
class Employee:
  def __init__(self, ID, salary):
    self.ID = ID
    self.__salary = salary # salary is a private property

Steve = Employee(3789, 2500)
print(Steve._Employee__salary) #accessing a private property