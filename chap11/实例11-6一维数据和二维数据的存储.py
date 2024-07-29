#存储和读取一维数据
def my_write():
    #一维数据，可以用列表，元组，集合
    lst=['szy','zm']
    with open('student.csv','w')as file:
        file.write(','.join(lst))#必须将列表转成字符串才能写入

def my_read():
    with open('student.csv','r')as file:
        s=file.read()
        lst=s.split(',')#读取时，将字符串转成列表
        print(lst)

#存储和读取二维数据
def my_write_table():
    lst=[
        ['名称','单价','采购数量',],
        ['水杯', '98.5', '20', ],
        ['鼠标', '39', '100', ],
    ]
    with open('table.csv','w',encoding='utf-8')as file:
        for item in lst:#item的数据类型是列表
            line=','.join(item)
            file.write(line)
            file.write('\n')
def my_read_table():
    data=[]
    with open('table.csv','r',encoding='utf-8')as file:
        lst=file.readlines()
        # print(type(lst),lst)
        for item in lst:#item是字符串类型
            new_lst=item[0:len(item)-1].split(',')
            data.append(new_lst)
    print(data)
if __name__ == '__main__':
    # my_write()
    # my_read()
    my_write_table()
    my_read_table()