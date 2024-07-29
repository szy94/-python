i=0
while i<3:
    user_name=input('请输入用户名：')
    password=input('请输入你的密码：')
    if user_name=='szy' and password=='888888':
        print('登陆成功！')
        i=4
    else:
        if i<2:
            print('用户名或者密码不正确,你还有',2-i,'次机会')
        i+=1
if i==3:
    print('三次全错，十分钟之后再尝试')