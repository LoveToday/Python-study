# Python-study
Python基础

1.python几种常见的数据类型

    A. Numbers(数字)->(1.int(有符号整型)2.long(长整型也可以代表八进制和十六进制)3.float(浮点型)4.complex(复数))
    B. 布尔类型->(True, False)
    C. String(字符串)
    D. List(列表)
    E. Tuple(元组)
    F. Dictionary(字典)
    
怎样知道一个变量的类型
    
    在Python中，只要定义了一个变量，而且它有数据，那么它的类型就已经确定了，
    不需要咱们开发者主动的去说明它的类型，系统会自动辨别
    
2.标识符

    标识符只能由字母、下划线和数字组成，但不能以数字开头；
    python中的标识符是区分大小写的
    命名规则：1.见名知意 2.驼峰命名法
    
3.关键字
    
    编译器自带关键字，不予许用于命名变量函数类
    使用keyword.kwlist查看关键词
    【False, None, True, and, as, assert, break, class,...
    
4.输入、输出

    input是输入，print是输出
    myString = input('请输入数据')
    print(myString)
    os.system(myString)

5.变量赋值的原理

    type(var) 求var的类型
    print(type(13))
    class 'int'
    
    id(var)内存地址
    print(id(13))
    1459008960
    
6.注释

    A.多行注释
    '''
    多行注释
    1
    2
    3
    end
    '''
    B.# 单行注释
    
7.变量赋值的原理

    python变量可以改变数据类型
    原理就是地址赋值
    num1 = 10
    print(num1)
    print(type(num1))
    num1 = 20
    print(num1)
    print(type(num1))
    num1 = "calc"
    print(type(num1))
    
8.复数数据类型

    复数
    data = 1+2j
    print(data)
    print(type(data))
    <class 'complex'>
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
