import re
pattern='\d\.\d+'
s=' I stduy Python3.11 every day Python2.7 I love you'
match=re.search(pattern,s)
s1='4.10 Python I study every day'
s2=' I study Python every day'
match1=re.search(pattern,s1)
print(match1)
print(match)
match2=re.search(pattern,s2)
print(match2)
print(match.group())
print(match1.group())
#print(match2.group())