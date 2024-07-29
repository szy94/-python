number=eval(input('请输入你的六位中奖号码:'))
if number==666666:
    print('666')
else:
    print('555')
print('恭喜你中奖了'if number==666666 else '你没中')