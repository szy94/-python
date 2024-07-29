'''
str.isdigit()验证所有的字符都是十进制阿拉伯数字（1，2，3，4，5）
str.isnumeric()所有的字符都是数字（1，2，3，罗马数字，一，二，三,壹，贰）
str.isalpha()所有字符都是字母，包括中文字符
str.isalnum()所有字符都是数字或者字母包含中文字符
str.islower()所有字符都是小写
str.isupper()所有字符都是大写
str.istitle()所有字符都是首字符大写
str.isspace()所有的字符都是空白字符
'''
print('123'.isdigit())
print('0b10101'.isdigit())
print('一'.isdigit())
print('一'.isnumeric())
print('壹'.isnumeric())
print('1235'.isnumeric())
print('011010'.isnumeric())
print('0b011010'.isnumeric())
print('&'*100)
print('szy你好'.isalpha())
print('szy你好123'.isalpha())
print('szy你好一'.isalpha())
print('szy'.isalpha())
print('szy123'.isalnum())
print('sazy'.islower())
print('SFS'.isupper())
print('Szyzm'.istitle())
print('    '.isspace())
print('*'*101)
print('szy你好'.islower())
print('ADZ你好'.isupper())
print('*'*101)
print('Hello孙志宇'.istitle())
print('Hello World'.istitle())
print('HelloWorld'.istitle())
print('Helloworld'.istitle())
print('Hello world'.istitle())
print('*'*101)
print('\t'.isspace())
print(' '.isspace())
print('\n'.isspace())
print('*'*101)
print(10/2)