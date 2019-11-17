import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))

# result=re.match('^Hello\s\d{7}\s\w{10}\s\w\w\s\w\s\w{5}\s\w{4}',content)
# print(result)
# print(result.group())
# print(result.span())

#匹配目标
# result=re.match(r'Hello\s(\d+)\sWorld',content)
# print(result)
# print(result.group())#输出完整的匹配结果
# print(result.group(1))#输出第一个被（）包围的匹配结果
# print(result.span())#输出匹配长度


#通用匹配
# result=re.match(r'Hello.*Demo',content)#.(点)可以匹配任意字符（除了换行符），*（星）代表匹配前面的字符无限次
# print(result)
# print(result.group())
# print(result.span())


#result=re.match(r'Hello.*Demo',content，re.S)加上re.S后。*可以匹配换行符

