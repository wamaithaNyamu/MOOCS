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