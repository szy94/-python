'''
format()
len(s)
id(obj)
type(x)
eval(s)
'''
print(format(3.14,'20'))#数值型默认右对齐
print(format('hello','20'))#字符串默认左对齐
print(format('hello','*<20'))#<表示左对齐，*表示填充符，20表示显示的宽度
print(format('hello','*>20'))#右对齐
print(format('hello','*^20'))#居中对齐


print(format(3.1415926,'.2f'))
print(format(20,'b'))
print(format(20,'o'))
print(format(20,'x'))
print(format(20,'X'))
print('*'*100)
print(len('helloworld'))
print(len([10,20,30,40,50]))
print('*'*100)
print(id(10))
print(id('helloworld'))
print(type('hello'),type(10))
print(eval('10+30'))
print(eval('10>30'))