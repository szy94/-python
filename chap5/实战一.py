lst=[88,89,90,98,00,99]
print(lst)
for i in range(len(lst)):
    if str(lst[i])!='0':
        lst[i]='19'+str(lst[i])
    else:
        lst[i]='200'+str(lst[i])
print(lst)