#定义一个列表
# name1=['张三','李四','王五']
# age1=[18,19,20]
# height=[170,180,190]
# weight=[50,60,70]
# print('姓名:',name1,'\n','年龄:',age1,'\n','身高:',height,'\n','体重:',weight)

# l1=['a','b','c','d'',e','f','g',]
# l2=['abcdefg']
# for i in l1:
#     print(i)
# for i in l2:
#     print(i)
lst=[1,2,3,4,5]
a,b,c,*d=lst
print(a,b,c,d)
a,b,c,d,e,*f=lst
print(a,b,c,d,e,f)