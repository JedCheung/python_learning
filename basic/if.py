# -*- coding:utf-8 -*-
print('Please input weights (kg):')
weights = input()
weights = float(weights)
print('Please input heights (m):')
heights = input()
heights = float(heights)
bmi = weights / (heights*heights)
print(bmi)

if bmi > 32:
    print('严重肥胖')
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')
