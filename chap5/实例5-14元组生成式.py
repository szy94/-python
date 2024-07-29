t=(i for i in range(1,4))
print(t)
#t=tuple(t)
#print(t)
#for i in t:
#    print(i)
print(t.__next__())
print(t.__next__())
print(t.__next__())#取出后元组当中就没有元素了

t=tuple(t)
print(t)