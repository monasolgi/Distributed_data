#This is the implementation of tutorial_01.
#Write a Python program that functions as a calculator.

#A. Your code should contain functions for each calculation type (addition, subtraction, ...)
#Each function takes two parameters as input, calculates the result and returns it

def summation(arg1, arg2):
    return arg1 + arg2

def multiply(arg1, arg2):
    return arg1 * arg2

def divide(arg1, arg2):
    return arg1 / arg2

def subtract(arg1, arg2):
    return arg1 - arg2

print("summation=",summation(1,2))
print("multiply=",multiply(1,2))
print("divide=",divide(1,2))
print("subtract=",subtract(1,2))

#-------------------------------------------------------------------------

#B. Add a dot product function that computes a multiplication-summation between two lists, numpy arrays or
#other list-like parameters:
#[a1, a2, a3] ⊙ [b1, b2, b3] = a1 ∗ b1 + a2 ∗ b2 + a3 ∗ b3

import numpy as np

def dot_product(a,b):
    return np.dot(a,b)

print("dot_product=",dot_product([1,2,3],[3,4,5]))

#--------------------------------------------------------------------------

#C. Design a control mechanism that allows you to interact with your calculator via the terminal.
#To obtain user-input in Python you can use input("prompt")
print("If you want to quit, type q")
user_input=input("Enter an operation:(+,*,/,-)")

while True:
    if user_input== "q":
        break
    if user_input not in ("+,*,/,-"):
        print("Invalid input")
        user_input=input("Enter a valid operation:(+,*,/,-)")


    if user_input=="+":
        first_arg=float((input("Enter your first number")))
        second_arg =float((input("Enter your second number")))
        print("summation=",summation(first_arg,second_arg))
        break

    if user_input=="*":
        first_arg=float((input("Enter your first number")))
        second_arg =float((input("Enter your second number")))
        print("multiply=",multiply(first_arg,second_arg))
        break

    if user_input=="/":
        first_arg=float((input("Enter your first number")))
        second_arg=float(input("Enter your second number"))
    if(second_arg==0):
            print("Error:Division by zero")
            break

    print("division",divide(first_arg,second_arg))
    break

    if user_input=="-":
        first_arg = float((input("Enter your first number")))
        second_arg = float(input("Enter your second number"))
        print("subtract", subtract(first_arg, second_arg))
        break

#-----------------------------------------------------------------

#2. Object Orientation
#Re-implement your calculator in an object-oriented fashion.
#A. Your calculator script now creates a top-level object of class Calculator that inherits all the functionality
#from before
#B. Every function (summation, etc.) you have written before becomes its own class.
#Every calculation class implements a calculate(arg1, arg2) function that can be called by the top-level
#Calculator class.
#Instead of separate functions, the calculator now has a collection of calculation objects that handle the math
#operations.
#C. Create a base class called Calculation that prescribes an abstract function calculate(arg1, arg2) and
#have every calculation class inherit from this base class
class Calculation:
    def calculate(self, arg1, arg2):
        raise NotImplementedError


class Addition(Calculation):
    def calculate(self, arg1, arg2):
        return arg1 + arg2


class Multiplication(Calculation):
    def calculate(self, arg1, arg2):
        return arg1 * arg2


class Division(Calculation):
    def calculate(self, arg1, arg2):
        if arg2 != 0:
            return arg1 / arg2
        else:
            raise ValueError("Error: Division by zero is not allowed.")


class Subtraction(Calculation):
    def calculate(self, arg1, arg2):
        return arg1 - arg2


class Calculator:
    def __init__(self):
        self.Calculations = {
            '+': Addition(),
            '*': Multiplication(),
            '/': Division(),
            '-': Subtraction()
        }

    def calculate_call(self, operator, arg1, arg2):
        return self.Calculations[operator].calculate(arg1, arg2)

    def run(self):
        print("Hello, Welcome to my calculation program. Whenever you want to quit, type 'q'.")

        while True:
            user_input = input("Enter an operation (+, *, /, -): ")

            if user_input == 'q':
                print("Bye! Hope to see you again.")
                break

            if user_input not in ('+', '*', '/', '-'):
                print("Invalid input.")
                user_input = input("Enter a valid operation (+, *, /, -): ")

            user_input_arg1 = float(input("Enter a number: "))
            user_input_arg2 = float(input("Enter a second number: "))

            try:
                result = self.calculate_call(user_input, user_input_arg1, user_input_arg2)
                print("Result:", result)
                print("-------------------------")
            except ValueError as e:
                print(e)
                print("-------------------------")


cal = Calculator()
cal.run()
