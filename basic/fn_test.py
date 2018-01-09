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


def product(*numbers):
    if numbers is ():
        raise TypeError('Please input int or float!')
    mul = 1
    for n in numbers:
        mul = mul * n
    return mul


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

# 利用递归函数移动汉诺塔:

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)#本次成功的倒数第三步必定是把 a上（n-1）个盘子通过c移动到b
        move(1, a, b, c)   # 本次成功的倒数第二步必定是把 1个盘子由a移动到c
        move(n - 1, b, a, c)  # 本次成功的倒数第一步必定是把b上 （n-1）个盘子通过a移动到c


move(4, 'A', 'B', 'C')
