lst=[]
for i in range(5):
    goods=input("请输入商品的编号和名称，进行商品入库，每次只能输入一次商品:")
    lst.append(goods)
for i in lst:
    print(i)

cart=[]
while True:
    flag=False
    num=input('请输入要购买的商品编号:')
    for i in lst:
        if num==i[0:4]:
            flag=True
            cart.append(i)
            print('商品已经成功添加到购物车')
            break
    if flag!=True and num!='q':
        print('商品不存在')
    if num=='q':
        break
print('-'*100)
print('购物车中您选择的商品为：')
cart.reverse()
for i in cart:
    print(i)