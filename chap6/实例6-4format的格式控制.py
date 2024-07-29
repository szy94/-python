s='helloworld'
print('{0:@<20}'.format(s))#字符串的显示宽度为20，<左对齐，空白部分用@填充，：是引导符号
print('{0:^>20}'.format(s))#>右对齐
print('{0:^^20}'.format(s))#居中对其
print(s.center(20,'&'))
#千位分隔符（只适用于整数和浮点数，字符串不行）
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.5468955))
#浮点数小数部分的精度
print('{0:.2f}'.format(3.1415926))#.2f保留两位小数
#若为字符串类型.表示的是最大显示长度
print('{0:.5}'.format('helloworld'))#.5表示最大显示长度
#整数类型
a=425
print('{0:b}'.format(a))
print('{0:o}'.format(a))
print('{0:d}'.format(a))
print('{0:x}'.format(a))
print('{0:X}'.format(a))
#浮点数类型
b=12.26589875
print('{0:.2f}'.format(b))
print('{0:.2e}'.format(b))
print('{0:.2E}'.format(b))
print('{0:.2%}'.format(b))