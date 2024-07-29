'''
元字符    描述说明
^         匹配的开始
$         匹配的结束
.         匹配任意字符（除\n）
\w        匹配字母，数字，下划线
\W        匹配非字母，非数字，非下划线
\s        匹配任意空白字符，如：\t
\S        匹配任意非空白字符
\d        匹配任意十进制数
'''
import re
pattern='\d\.\d+'#+限定符，\d 0-9数字出现1次或多次
s='I study Python 3.11 every day'#待匹配字符串
match=re.match(pattern,s,re.I)#re.I表示忽略大小写，i=ignore
print(match)
s2='3.11Python I study every day'
match1=re.match(pattern,s2)
print(match1)
print(match1.start())
print(match1.end())
print(match1.span())
print(match1.string)
print(match1.group())
'''
限定符    匹配次数      
？       0次或一次
+        1次或多次
*        0次或多次
{n}         n次
{n，}     至少n次
{n，m}  最少n次，最多m次
'''
