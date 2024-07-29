'''
函数名                         描述说明
json.dumps(obj)                将Python数据类型转成JSON格式过程，编码过程
json.loads(s)                  将JSON格式字符串转成Python数据类型，解码过程
json.dump(obj, file)           与dumps（）功能相同，将Python数据类型转成JSON格式过程，将转换结果存储到文件file
json.load(file)                与loads（）功能相同，将JSON格式字符串转成Python数据类型，从文件file中读入数据

'''
import json
#准备高维数据
lst=[
    {'name':'szy','age':18,'score':90},
    {'name':'dzm','age':19,'score':100},
    {'name':'wxy','age':20,'score':80}
]
s=json.dumps(lst,ensure_ascii=False,indent=4)#ensure_ascii=False为了正常显示中文，防止乱码，indent=4增加数据的缩进，为了美观
print(type(s),s)
lst2=json.loads(s)
print(type(lst2),lst2)
#编码到文件当中
with open('student.txt','w')as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)
#从文件当中解码
with open('student.txt','r')as file:
    lst3=json.load(file)#直接是列表类型
    print(type(lst3))
    print(lst3)