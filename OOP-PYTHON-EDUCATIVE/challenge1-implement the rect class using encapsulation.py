# Problem Statement #
#
# You are given a partially completed code of a Rectangle class in the editor. Implement the class by completing the tasks below.
# Task 1 #
#
# Implement a constructor to initialize the values of two private properties: length and width.
# Task 2 #
#
# Implement a method, area(), in the Rectangle class that returns the product of length and width. See the formula below:
#
# Area=length×widthArea = length \times widthArea=length×width
#

class Rectangle():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def Area(self):
       a = self.__length * self.__width
       return a


    def Perimeter(self):
       a = self.__length + self.__width
       return a * 2

z =Rectangle(4,5)
z.Area()
z.Perimeter()