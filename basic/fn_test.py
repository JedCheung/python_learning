# -*- coding: utf-8 -*-
""" This is a python fn test demo. """
import math

def quadratic(a, b, c):   
    """this is a fn for cal the roots of ax^2 + bx + c = 0"""
    if a == 0:
        print('a can not be 0!')
    if not isinstance(a, (int, float)):
        raise TypeError('The input should be int or float')
    if not isinstance(b, (int, float)):
        raise TypeError('The input should be int or float')
    if not isinstance(c, (int, float)):
        raise TypeError('The input should be int or float')
    r1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    r2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return r1, r2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
