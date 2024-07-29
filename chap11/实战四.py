def find_answer(question):
    with open('reply.txt','r',encoding='utf-8')as file:
        while True:
            line=file.readline()
            if line=='':
                break
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return False
if __name__ == '__main__':
    question=input('输入你的问题：')
    while True:
        if question=='bye':
            break
        else:
            reply=find_answer(question)
            if reply==False:
                question=input('不知道你在说什么,你可以问我一些关于订单，物流，支付，账户方面的问题,退出请输入bye：')
            else:
                print(reply)
                question=input('你还可以问一些关于订单，物流，支付，账户方面的问题，退出请输入bye：')
    print('再见')