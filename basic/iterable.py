# -*- coding: utf-8 -*-
def findMinAndMax(L): 
    """请使用迭代查找一个list中最小和最大值，并返回一个tuple："""
    if L == []:
        minnum, maxnum = None, None
    else:
        minnum, maxnum = L[0], L[0]
        for num in L:
            if num < minnum:
                minnum = num
            if num > maxnum:
                maxnum = num
    return (minnum, maxnum)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
