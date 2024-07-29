'''
abs(x)           获取x的绝对值
divmod(x,y)      获取x与y的商和余数
max(sequence)    获取最大值
min(sequence)    获取最小值
sum(iter)        对可迭代对象进行求和运算
pow(x,y)         获取x的y次幂
round(x,d)       对x进行保留d位小数，结果四舍五入
'''
print(abs(-20))
print(divmod(10,3))
print(max(10,12,9,50))
print(max([10,20,30,40]))
print(min([10,20,30,40]))
print(max('hello'))
print(sum([10,34,45]))
print(pow(2,3))
print(round(3.1415926,2))
print(round(3.1415926))#若不写d，则默认保留整数
print(round(3.1415926,-1))
print(round(314.15926,-1))#对个位进行四舍五入
print(round(315.15926,-1))
print(round(314.15926,-2))#对十位进行四舍五入