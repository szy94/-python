t=('python','hello','world')
print(t[0])
t2=t[0:3:2]
print(t2)
#元组的遍历
for i in t:
    print(i)
for i in range(len(t)):
    print(t[i])
for index,item in enumerate(t):
    print(index,item)