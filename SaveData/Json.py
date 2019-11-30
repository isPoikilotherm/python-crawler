import json


#读取JSON
str='''
[{
"name":"yangliu",
"gender":"male",
"birthday":"1992-12-25"
},{
"name":"yang",
"gender":"female",
"birthday":"1999-01-11"
}]
'''
print(type(str))
data=json.loads(str)
print(data)
print(data[0])
print(data[0]['name'])
print(data[0].get('name'))
print(type(data))


#输出JSON
data_1=[
    {
        'name':'Bob',
        'gender':'male',
        'birthday':'1996-10-01'
    }
]
data_2=[
    {
        'name':'张三',
        'gender':'男',
        'birthday':'1996-10-01'
    }
]
with open('data.json','w') as file:
    file.write(json.dumps(data_1,indent=2))#indent表示缩进字符个数

with open('data2.json', 'w',encoding='utf-8') as file:#JSON中包含中文字符时，要指明编码格式
        file.write(json.dumps(data_2, indent=2,ensure_ascii=False))  #JSON中包含中文字符时，ensure_ascii设为False