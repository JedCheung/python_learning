# -*- coding: utf-8 -*-

def trim(s):
    """利用切片操作，实现一个trim()函数，
    去除字符串首尾的空格，注意不要调用str的strip()方法"""

    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s


# def trim(s):
#     if s == '':
#         return s
#     elif s[0] == ' ':
#         return trim(s[1:])
#     elif s[-1] == ' ':
#         return trim(s[:-1])
#     return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
