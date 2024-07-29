a=100

def calc(x,y):
    return a+x+y
print(a)
print(calc(10,20))

print('*'*100)
def calc2(x,y):
    a=200#局部变量的名称和全局变量的名称相同
    return a+x+y#这里所加的a是全局变量a=100还是局部变量a=200呢？
print(calc2(10,20))#输出230，使用的a是局部变量a=200
print(a)#这里输出的a是100还是200呢？输出的是a=100
print('*'*100)
def calc3(x,y):
    global s
    s=300
    return s+x+y
print(calc3(10,20))
#s=500
print(s)