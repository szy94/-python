answer=input('你喝酒了没？:')
if answer=='y':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('不是酒驾')
    elif proof<80:
        print('酒驾！')
    else:
        print('醉驾')
else:
    print('走吧')