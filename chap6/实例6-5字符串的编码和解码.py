s='伟大的中国梦'
#编码：str.encode（），将str转换成bytes
#解码：bytes.decoding，将bytes转成str
scode=s.encode(errors='replace')#默认utf-8，utf-8中文默认占3个字节
print(scode)
scode_gbk=s.encode('gbk',errors='replace')
print(scode_gbk)

#编码中的出错问题
s2='耶🖐️'
scode=s2.encode('gbk',errors='ignore')#忽略
print(scode)
#scode=s2.encode('gbk',errors='strict')#严格
#print(scode)
scode=s2.encode('gbk',errors='replace')#替换成？
print(scode)


#解码过程
print(bytes.decode(scode_gbk,'gbk'))