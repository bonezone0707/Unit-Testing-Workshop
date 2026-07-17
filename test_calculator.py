"""
Unit Test File

This file contains pytest unit tests for the calculator module.

Each test checks one specific behavior and uses assertions
to verify that the function produces the expected result.
"""


# Import pytest so we can use testing features such as
# checking for expected errors.
import pytest


# Import the calculator functions that will be tested.
from calculator import add, subtract, multiply, divide



# -------------------------------
# Test 1: Addition Function
# -------------------------------

# This test verifies that the add function correctly
# adds two positive numbers together.
#
# Expected behavior:
# add(2,3) should return 5.
def test_add_positive_numbers():

    # Assert checks that the actual result matches
    # the expected result.
    assert add(2, 3) == 5



# -------------------------------
# Test 2: Subtraction Function
# -------------------------------

# This test checks that subtraction works when
# the answer becomes a negative number.
#
# This represents an edge case because many programs
# need to handle negative values correctly.
#
# Expected behavior:
# subtract(5,10) should return -5.
def test_subtract_negative_result():

    # Verify that the subtraction output is correct.
    assert subtract(5, 10) == -5



# -------------------------------
# Test 3: Multiplication Function
# -------------------------------

# This test verifies multiplication when one input
# is zero.
#
# This is an important boundary condition because
# any number multiplied by zero should equal zero.
#
# Expected behavior:
# multiply(8,0) should return 0.
def test_multiply_by_zero():

    # Confirm the function correctly handles zero.
    assert multiply(8, 0) == 0



# -------------------------------
# Test 4: Division Function
# -------------------------------

# This test verifies normal division behavior.
#
# Expected behavior:
# divide(10,2) should return 5.
def test_divide_normal():

    # Confirm that normal division works correctly.
    assert divide(10, 2) == 5



# -------------------------------
# Test 5: Division By Zero
# -------------------------------

# This test checks that the program properly handles
# an invalid input.
#
# Dividing by zero should not crash the program.
# Instead, it should raise a ValueError.
#
# Expected behavior:
# divide(10,0) raises ValueError.
def test_divide_by_zero():

    # pytest.raises verifies that the expected error occurs.
    with pytest.raises(ValueError):

        # This line should trigger the ValueError.
        divide(10, 0)
