# msg ='tom's phone number is 110'#会报错
# print(msg)
# #可以写成
msg ='tom\'s phone number is 110'  #转义字符 \,  \\r 会输出\r
print(msg)
#或者
# msg =R'tom's phone\r number is 110\n ' #原生字符,需要在保证语法正确的前提下去使用
msg =R"tom's phone\r number is 110\n "  #原生字符，可以使所有输入的值和符号按照输入的内容去输出
print(msg)



