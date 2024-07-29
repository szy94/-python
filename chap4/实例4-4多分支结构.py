score=eval(input('请输入你的成绩：'))
if score>100 or score<0:
    print('你输入的成绩有误')
elif score>=90 and score<=100:
    print('优秀')
elif score>=80 and score<90:
    print('良好')
elif score>=70 and score<80:
    print('还行')
else:
    print('laji')