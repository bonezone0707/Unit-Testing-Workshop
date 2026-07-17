"""
Calculator Module

This file contains basic calculator functions that perform
common mathematical operations. These functions will be tested
using the pytest unit testing framework.
"""


# This function takes two numbers and returns their sum.
# Example: add(2, 3) returns 5.
def add(a, b):
    """
    Adds two numbers together.

    Parameters:
        a: First number
        b: Second number

    Returns:
        The result of adding a and b.
    """
    return a + b


# This function subtracts the second number from the first number.
# It supports both positive and negative results.
# Example: subtract(5, 10) returns -5.
def subtract(a, b):
    """
    Subtracts one number from another.

    Parameters:
        a: Starting number
        b: Number being subtracted

    Returns:
        The result of a minus b.
    """
    return a - b


# This function multiplies two numbers together.
# It also handles edge cases such as multiplying by zero.
# Example: multiply(8, 0) returns 0.
def multiply(a, b):
    """
    Multiplies two numbers.

    Parameters:
        a: First number
        b: Second number

    Returns:
        The result of multiplying a and b.
    """
    return a * b


# This function divides one number by another.
# A check is included to prevent division by zero,
# because dividing by zero is mathematically invalid.
def divide(a, b):
    """
    Divides one number by another.

    Parameters:
        a: Number being divided
        b: Number dividing a

    Returns:
        The result of a divided by b.

    Raises:
        ValueError:
        If the user attempts to divide by zero.
    """

    # Check for the invalid edge case of dividing by zero.
    if b == 0:
        raise ValueError("Cannot divide by zero")

    # If the divisor is valid, perform the division.
    return a / b
