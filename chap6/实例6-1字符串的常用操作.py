'''
str.lower()转小写
str.upper（）转大写
str.split(sep=None)把str按照指定的分隔符sep进行分隔，结果为列表类型
str.count(sub)统计sub这个字符串在str中出现的次数
str.find(sub)查找sub这个字符串在str中是否存在，如不存在报-1，若存在结果为sub首次出现的索引
str.index(sub)功能与find相同，区别在于要查询的子串sub不存在时程序会报错
str.startswith(s)查询字符串str是否以子串s开头
str.endswith(s)查询字符串str是否以子串s结尾
str.replace(odd,news)使用news替换字符串中的所有old字符串，结果是一个新的字符串
str.center（width，fillchar）字符串str在指定的宽度范围内居中，可以使用fillchar进行填充
str.join（iter）在iter中的每个元素后面都增加一个新的字符串str
str.strip（chars）从字符串中去掉左侧和右侧chars中列出的字符串
str.lstrip（chars）从字符串中去掉左侧chars中列出的字符串
str.rstrip（chars）从字符串中去掉右侧chars中列出的字符串
'''
s='hello'
s1=str.upper(s)
print(s1)
s2=str.lower(s1)
print(s2)
e_mail='szy@126.com'
lst=e_mail.split('@')
print(lst)
print(s.count('o'))
print(s.find('o'))
print(s.find('s'))
#print(s.index('s'))
print(s.startswith('h'))
print(s.startswith('s'))
print(s.endswith('o'))
print(s.endswith('s'))

print('001.jpg'.endswith('.jpg'))
print('text.txt'.endswith('.txt'))

s='hello'
s1=s.replace('l','s',2)
print(s1)
print(s.center(20,'*'))
s='szy  Hello   World szy'
print(s.strip('szy'))
print(s.lstrip('szy'))
print(s.rstrip('szy'))
s3='ld oo dl'
print(s3.strip('ld'))#ld dl都会被去除,与顺序无关
print(s3.strip('dl'))