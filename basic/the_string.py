# -*- coding: utf-8 -*-
""" This is a python string test demo. """
S1 = 72
S2 = 85
IMPROVEMENT = 100.0 * (S2-S1)/S1
print('Name: %s Age: %s Gender: %s' % ("小明", 5, True))
print('Score in the past two years: S1: %d, S2: %d' % (S1, S2))
print('improvemt: %.1f %%' % IMPROVEMENT)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0], L[1][1], L[2][2])
print('Done!')
