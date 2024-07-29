#遍历字符串
for i in 'hello':
    print(i)


for i in range(1,11):#包含1不包含11
    #print(i)#四个字符为一个缩进
    if i%2==0:
        print(i,'是偶数')
sum=0
for i in range(1,11):
    sum+=i;
print(sum)
print('_'*100)
