class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        Vehicle.__init__(self, make, color, model)  # calling the constructor from parent class
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()


# Explanation #
#
#     In the code above, we have defined a parent class, Vehicle, in line 1 and a child class, Car, in line 12.
#
#     Car inherits all the properties and methods of the Vehicle class and can access and modify them.
#
#     For example in line 18 of the Car class, we have called the printDetails() method, which was actually defined in the Vehicle class, in the printCarDetails() method.
#
#SUPER FUNCTION
class Vehicle:
    def display(self):
        print('the parent class')
class MyCar(Vehicle):
    def display(self):
        super().display()
        print('my car classs')

car = MyCar()
car.display()

# SUPER METHOD USING INTITALISERS
class ParentClass():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class ChildClass(ParentClass):
    def __init__(self, parentname, parentgender, bday, age):
        super().__init__(parentname, parentgender)
        self.bday = bday
        self.age= age


child = ChildClass('John', 'M', 'April', 3)

# TYPES OF INHERITANCE


# Single Inheritance #
#
# In single inheritance, there is only a single class extending from another class. We can take the example of the Vehicle class, as the parent class, and the Car class, as the child class.

# MULTILEVEL

class Vehicle: #parent class
  def setTopSpeed(self, speed): #defining the set
    self.topSpeed = speed
    print("Top speed is set to", self.topSpeed)

class Car(Vehicle): #child class of Vehicle
  def openTrunk(self):
    print("Trunk is now open.")

class Hybrid(Car): #child class of Car
  def turnOnHybrid(self):
    print("Hybrid mode is now switched on.")

priusPrime = Hybrid() #creating an object of the Prius class
priusPrime.setTopSpeed(220) #accessing methods from the parent class
priusPrime.openTrunk() #accessing method from the parent class
priusPrime.turnOnHybrid() #accessing method from the parent class



# Hierarchical Inheritance #

class Vehicle: #parent class
  def setTopSpeed(self, speed): #defining the set
    self.topSpeed = speed
    print("Top speed is set to", self.topSpeed)

class Car(Vehicle): #child class of Vehicle
    pass

class Truck(Vehicle): #child class of Car
  pass

corolla = Car() #creating an object of the Prius class
corolla.setTopSpeed(220) #accessing methods from the parent class

volvo = Car() #creating an object of the Prius class
volvo.setTopSpeed(180) #accessing methods from the parent class

# Multiple Inheritance



class CombustionEngine(): #Child class inherited from Engine
  def setTankCapacity(self, tankCapacity):
    self.tankCapacity = tankCapacity

class ElectricEngine(): #Child class inherited from Engine
  def setChargeCapacity(self, chargeCapacity):
    self.chargeCapacity = chargeCapacity

#Child class inherited from CombustionEngine and ElectricEngine
class HybirdEngine(CombustionEngine, ElectricEngine):
  def printDetails(self):
    print("Tank Capacity:", self.tankCapacity)
    print("Charge Capacity:", self.chargeCapacity)

car = HybirdEngine()
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
# Hybrid inheritance.

class Engine: #Parent class
  def setPower(self, power):
    self.power = power

class CombustionEngine(Engine): #Child class inherited from Engine
  def setTankCapacity(self, tankCapacity):
    self.tankCapacity = tankCapacity

class ElectricEngine(Engine): #Child class inherited from Engine
  def setChargeCapacity(self, chargeCapacity):
    self.chargeCapacity = chargeCapacity

#Child class inherited from CombustionEngine and ElectricEngine
class HybirdEngine(CombustionEngine, ElectricEngine):
  def printDetails(self):
    print("Power:", self.power)
    print("Tank Capacity:", self.tankCapacity)
    print("Charge Capacity:", self.chargeCapacity)

car = HybirdEngine()
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()























