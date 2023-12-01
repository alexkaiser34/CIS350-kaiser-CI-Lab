from math_functions import *


def test_calc_addition():
    output = add_numbers(2,4)
    assert output == 6


def test_calc_subtraction():
    output = subtract_numbers(2, 4)
    assert output == -2

def test_calc_multiply():
    output = multiply_numbers(2,4)
    assert output == 8

def test_calc_divide_and_floor():
    output = divide_and_floor_numbers(11,2)
    assert output == 5

def test_calc_modulus():
    output = modulus_numbers(10,3)
    assert output == 1 


def test_calc_divide():
    output = divide_numbers(10,2)
    assert output == 5
