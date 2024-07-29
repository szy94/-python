#使用占位符格式化字符串
name='szy'
age=18
score=156.56
print('姓名：%s,年龄：%d,成绩：%f'% (name,age,score))




#使用f，{}格式化字符串，用{}标记要被替换的字符
print(f'姓名：{name},年龄：{age},成绩：{score}')
s=set()
#for i in range(1,3):
 #   info = input(f'请输入第{i}位好友的姓名和手机号：')
  #  s.add(info)
#使用x.format（， ， ，）方法格式化字符串
print('姓名：{0}，年龄：{1}，成绩：{2}'.format(name,age,score))
print('姓名：{2}，年龄：{0}，成绩：{1}'.format(name,age,score))
#print('姓名：{2}，年龄：{4}，成绩：{4}'.format(name,age,score))