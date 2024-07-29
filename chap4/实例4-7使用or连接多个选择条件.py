score=eval(input('请输入你的成绩：'))
if score<0 or score>100:
    print('成绩无效！')
else:
    print('你的成绩是：',score)