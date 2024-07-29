s1='hello'
s2='world'
#（1）使用+进行拼接
print(s1+s2)
#(2)使用字符串的join方法进行拼接
print(''.join([s1,s2]))#使用空字符串进行拼接，str.join（）
print('*'.join(['hello','world','python','java','php']))#使用*进行拼接
print('你好'.join(['hello','world','python','java','php']))
#(3)直接拼接
print('hello''world')
#(4)使用格式化字符串进行拼接
print('%s%s' %(s1,s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1,s2))