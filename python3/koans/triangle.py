#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if (a == 0) and (b == 0) and (c == 0):
        raise TriangleError("All zeros")
    if (a < 0) or (b < 0) or (c < 0):
        raise TriangleError("Negative")
    if atLeastTwoSidesGreaterThanTheThird(a, b, c) == False:
        raise TriangleError("Invalid")


    if (a == b) and (b == c):
        return 'equilateral'
    if (a == b) or (b == c) or (a == c):
        return 'isosceles'
    else:
        return 'scalene'

def atLeastTwoSidesGreaterThanTheThird(a, b, c):
    if (a + b) <= c:
        return False
    if (b + c) <= a:
        return False
    if (c + a) <= b:
        return False
    else:
        return True

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
