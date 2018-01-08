# -*- coding: utf-8 -*-
""" This is a python dict and set test demo. """
DICT_INSTANCE = {'zhang':25, 'zhou':24, 'zhao':28}
print(DICT_INSTANCE)
print(DICT_INSTANCE['zhang'])
DICT_INSTANCE.pop('zhang')
print(DICT_INSTANCE)

SET_INSTANCE = set([1, 2, 3])
print(SET_INSTANCE)
#SET_INSTANCE.add(['qian', 'li'])
#print(SET_INSTANCE) #TypeError: unhashable type: 'list'
SET_INSTANCE.add('qian')
print(SET_INSTANCE)

TUPLE_INSTANCE = (4, 5, 6)
SET_INSTANCE.add(TUPLE_INSTANCE) #指向都不变的tuple可以添加进去
print(SET_INSTANCE)

TUPLE_INSTANCE = (4, [5, 6])
SET_INSTANCE.add(TUPLE_INSTANCE)  # 指向变的tuple不可以添加进去
print(SET_INSTANCE)
