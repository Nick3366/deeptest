# -*- coding:utf-8 -*-
#for元组遍历
ver = (1,2,3,4,5,6,7,8,9,10)
print ("遍历元组，并打印出来：")
for tt in ver :
     print (tt)
#for列表遍历
if  8==8:
    list = ["猫儿","水杯","手机"]
    print ("遍历列表，并打印出来")
    for text in list:
        print (text)
#for字典遍历
if 8 == 8:
    dict_1 = {"name":"Nick","age":"25"}
    print ("遍历字典方式一，并打印出来")
    for (key,value) in dict_1.items():
        print ("%s : %s" % (key ,value))
#换行+分界线
    print ("\n----------------------")

    print ("遍历字典方式二，并打印出来")
    for key in dict_1:
        print ("%s : %s" % (key ,dict_1[key]))

#range序列半开半闭区间
for i in range(0,10):
    print(i,end=',')
#换行
print ('')
#带步长方式生产序列进行遍历
for i in range(0,10,2):
    print(i,end=',')
#换行
print ('')
#使用默认参数度
for i in range(5):
    print (i,end=',')

print ("")
#for循环实现久久乘法表：
if 8==8:
    print ("九九乘法表")
    for i in range(1,10):
        for j in range(i,10):
            print ("%d * %d = %2d " % (i,j,i*j),end="  ")
        print ("")
if __name__=="__main__":
    print ("\n九九乘法口诀表")
    for i in range(1,10):
        for j in range(i,10):
            print ("%d * %d = %2d" % (i,j,i*j),end=" ")
        print ("")

if 9 ==9:
    print ("九九乘法表")
    for i in range(1,10):
        for j in range(i,10):
            print ("%d * %d = %2d" % (i,j,i*j),end=" ")
        print ("")

if __name__ == "__main__":
    print(u"计算0-100间所有偶数和")

    n = 100
    index = 0
    sum = 0
    while index <= n:
        sum = sum + index
        index = index + 2

    print(u"0-100间偶数和= %d " % sum)

print ("")


if 8 == 8 :
    print ("九九乘法表")
    n = 1

    while n <=  9 :
        for m in range(n,10):
            print ("%d * %d = %2d"%(n,m,n*m),end="")

        print ("")
        n = n+1




