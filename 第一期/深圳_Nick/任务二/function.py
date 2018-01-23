# -*- coding:utf-8 -*-
__author__ =u"Nick"
def sum(a,b):
    c = a+b
    return c

if 8 == 8:
    print("函数定义，求和：")
    #调用函数
    c =sum (1,2)
    print (c)

#九九乘法表
def multi():
    data = []
    for i in range(1,10):
        line = []
        for j in range(i,10):
            line.append(u"%d * %d = %2d" % (i,j,i*j))
        data.append(line)
    return data

if 8 == 8:
    print("九九乘法表")
    data = multi()
    for d in data:
        print (d)

#元组传递参数
#求和
def sum_tuple(seq):
    sum = 0
    for s in seq:
        sum = sum +s
    return sum

if 8 == 8 :
    print ("元组传参，求和")
    tuple_1 = (1,2,3,4,5,6,7,8,9,10)
    print (tuple_1)

    sum = sum_tuple(tuple_1)
    print("求和：%d" % sum)

#字符串连接函数
def str_join(str1,str2,str3):
    return str1 + str2 + str3

if 8 == 8 :
    str1 = "大家好"
    str2 = "我的名字:"
    str3 = "Nick"

str_j = str_join(str1,str2,str3)
print (str_j)
