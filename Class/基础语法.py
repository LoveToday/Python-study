
'''
编码
默认是v3 是UTF-8 可以指定不同编码 （# -*- coding: cp-1252 -*- ）
'''

'''
标识符
第一个字符必须是字母或者是下划线
标识符的其他部分有字母、数字、下划线组成
标识符对大小写敏感
'''

'''
关键字
import keyword
keyword.kwlist
print(keyword.kwlist)
['False', 'None', 'True', 
'and', 'as', 'assert', 'async', 
'await', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']
'''

# '''
# 注释
# 单行#
# 多行''' #或是 """
# '''

"""
行与缩进
不需要使用大括号
使用缩进表示代码块
"""

'''
多行语句
语句过长可以使用反斜杠
total_sum = one + \
            two + \
            tree
在[]、{}或是（）则不需要
'''

'''
数字（Number）类型
四种类型 int(整型) bool(布尔) float(浮点型) complex(复数)
'''

# 字符串（String）
# 单引号与双引号完全相同
# 使用三引号可以指定一个多行字符串
#eg:paragraph = """这是一个段落，
# 转移字符 \
# 反斜杠可以用来转义，使用可以让反斜杠不转义 如 r"this is a line with \n" 则\n会显示，并不是换行
# 可以用+连接 用*运算符重复
# 两种索引方式，从左向右0开始 从右向左 -1开始
# 字符串不能改变
# 没有单独的字符类型 一个字符就是长度为1的字符串
# 字符串的截取的语法是 变量[头下标：尾下标：步长]

'''
import 与 from...import
在python用 import 或者from...import来导入相应的模块
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''















      


