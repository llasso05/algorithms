"""Create a class Number that stores an integer.

Overload the + operator (__add__) to add two Number objects together.
Overload __str__ to return a readable format."""

class Number:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Number(self.number + other.number)
    
    def __str__(self):
        return f"Number: {self.number}"

n1 = Number(10)
n2 = Number(5)
n3 = n1 + n2  # Should return a new Number(15)
print(n3)  # Expected output: "Number: 15"

    
