import re

phone = "15639128975 #这是我的电话"
num = re.sub('#(.*?$)', "", phone)
print(num)

s = 'Hello word'
reg = re.compile('hello', re.I)
print(reg.match(s).group())
print(re.match('Hello', s).group())