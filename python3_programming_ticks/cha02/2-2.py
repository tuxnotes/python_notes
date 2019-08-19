#!/usr/bin/env python3

s = ('Jim',16,'male','jim8721@gmail.com')
t = (34, 'liushuo')
# 方案一，类似于C语言中的define,但Python不是编译型语言，没有预处理过程，直接赋值

#NAME = 0
#AGE = 1
#SEX = 2
#EMAIL = 3

# effective method than above

NAME, AGE, SEX, EMAIL = range(4)

# 枚举

from enum import IntEnum

class StudentEnum(IntEnum):
    NAME = 0
    AGE = 1
    SEX = 2
    EMAIL = 3

s[StudentEnum.NAME]

# 方案二，recommanded

from collections import namedtuple

Student = namedtuple('Student', ['name','age','sex'.'email'])
s2 = Student('Jim',16,'male','jim8721@gmail.com')

