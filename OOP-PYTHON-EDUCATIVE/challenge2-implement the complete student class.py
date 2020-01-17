# Problem Statement #
#
# Implement the complete Student class by completing the tasks below
# Task #
#
# Implement the following properties as private:
#
#     name
#     RollNumber
#
# #
#
# Include the following methods to get and set the private properties above:
#
#     getName()
#     setName()
#     getRollNumber()
#     setRollNumber()
#
# Implement this class according to the rules of encapsulation.
class Student:

    def setName(self, name):
        self.__name = name

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber

    def getName(self):
        return self.__name

    def getRollNumber(self):
        return self.__RollNumber

Alex = Student()
Alex.setName('Alex')
Alex.setRollNumber(1234)