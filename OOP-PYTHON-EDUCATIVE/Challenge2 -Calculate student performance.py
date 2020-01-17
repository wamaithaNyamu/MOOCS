# Problem Statement #
#
# Implement a class Student that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:
# Task 1 #
#
# Implement a constructor to initialize the values of four properties: name, phy, chem and, bio.
# Task 2 #
#
# Implement a method, totalObtained, in the Student class that calculates total marks of a student.
#
class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        total = self.phy + self.chem +self.bio
        return total
    def percentage(self):
        x = self.totalObtained() / 300 * 100
        return x

z =Student('Mark', 80 , 90, 40)
print(z.percentage())