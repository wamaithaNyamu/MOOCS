# Problem Statement #
#
# Write a Python class called Calculator by completing the tasks below:
# Task 1 #
# Initializer #
#
# Implement an initializer to initialize the values of num1 and num2.
# Properties #
#
#     num1
#     num2
#
# Task 2 #
# Methods #
#
#     add(), a method which returns the sum of num1 and num2.
#
#     subtract(), a method which returns the subtraction of num1 from num2.
#
#     multiply(), a method which returns the product of num1 and num2.
#
#     divide(), a method which returns the division of num2 by num1.
#

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 /  self.num1

obj = Calculator(10, 94);
obj.add()
obj.subtract()
obj.multiply()
obj.divide()