import random
#设置随机数的种子
random.seed(2)#设置之后第二次，第三次，第n次生成的随机数会与第一次生成的数保持一致
print(random.random())#生成一个[0.0,1.0）之间的小数
print(random.random())
print(random.uniform(1,10))#生成一个[a，b]之间的随机小数
print(random.randint(1,10))#生成一个[a,b]之间的整数
print(random.randrange(1,10,2))#生成一个[a，b）之间步长为2的随机整数
lst=[1,22,568,456]
print(random.choice(lst))#从序列中随机选择一个元素
random.shuffle(lst)#将序列中的元素随机排列，返回打乱后的序列
print(lst)
