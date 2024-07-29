s='3.14+3'
print(s,type(s))
x=eval(s)#使用eval函数去掉s这个字符串中左右的引号
print(x,type(x))
age1=input('请输入你的年龄：')#input输入的是字符串类型
print(age1,type(age1))
age2=eval(input('请输入你的年龄：'))#将字符串类型转成int类型，相当于int（age2）
print(age2,type(age2))