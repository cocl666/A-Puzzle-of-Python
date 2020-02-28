#!/usr/local/bin/python3
#指定python3为解释器
#输出
print('hello world1')
# >>> print('hello'+'world') 拼接
# helloworld

#缩进一般为4空格
if 3 > 10:
    print('yes')
print('ok')

#续行
print('hello',\
      'world2')

#print可以直接打印内容
print('hello world3')

#print也可以打印多项内容
print('hao',123)
print('hao','ya',123)

#sep间隔,end
print('hao',123,sep='***')
print('hao',123,sep='***',end='')

#help()帮助信息
#help(input)

#input输入
# >>> input("number:")
# number:20
# '20'
# >>> input()
# tom
# 'tom'
# >>> input()
# 10
# '10'
# >>> a=input()
# 10
# >>> print(a)
# 10
# >>> a+5报错，因为'10'是字符串
# >>> int(a)+5
# 15
# >>> a+str(5)
# '105'

#变量
#首字符必须是字母或下划线;
#后续字符必须是大小写字母或数字或下划线;
#区分大小写;
#一般采用的全名方法：1.变量名全部采用小写字母；2.多个单词间使用_分割；3.变量名用名词，函数名用(动词+名词);4.类名采用驼峰形式；
#变量赋值自右向左，将=右边的表达式计算出结果，赋值给左边变量
a=5+5
a=a+1
print(a)
#++a 只是指正正为正

import this #python之禅，美胜丑，明胜暗，简胜繁，操作的复杂胜理解的复杂

#算术运算符
# >>> 5/3
# 1.6666666666666667
# >>> 5%3 模运算，之保留余数
# 2
# >>> 5//3 只得到商
# 1
# >>> divmod(5,3) 5除以3的商和余数
# (1, 2)
# >>> a,b=divmod(5,3) 5除以3的商和余数，分别赋值给a,b
# >>> a
# 1
# >>> b
# 2
# >>> 2**3 2的3次方
# 8

#比较运算符
# >>> 3!=3
# False
# >>> 3==3
# True
# >>> 10<20<30 连续比较
# True
# >>> 10<20>15 可读性差，不建议使用
# True
# >>> 10>5 and 5>8 and两边全为真则为真，否则为假
# False
# >>> 10>5 or 5>8 or两边，有一边为真则为真，两边全为假才是假
# True
# >>> not 10>5 not取反，将真变假，假变真
# False

#数据类型
#int整数：没有小数点；float浮点数：有小数点；
#bool布尔值：True:1;False:0;
#complex复数

#python默认10进制
# >>> 0o11 8进制
# 9
# >>> 0O11
# 9
# >>> 0x11 16进制
# 17
# >>> 0X11
# 17
# >>> 0b11 2进制
# 3
# >>> 0B11
# 3
# >>> oct(10) 10转8
# '0o12'
# >>> hex(10) 10转16
# '0xa'
# >>> bin(10) 10转2
# '0b1010'

#python中字符串必须用引号引起来，单双引号无区别；支持三引号，用于保留字符串格式
# >>> words="""hello
# ... ni hao
# ... abc"""
# >>> print(words)
# hello
# ni hao
# abc
# >>> words2='aaa\nbbb\nccc\nddd'
# >>> print(words2)
# aaa
# bbb
# ccc
# ddd

#字符串切片
# >>> s1='python' 012345
# >>> s1[0]
# 'p'
# >>> s1[5]
# 'n'
# >>> s1[-1]
# 'n'
# >>> s1[-6]
# 'p'
# >>> s1[2:3] 取切片不包含结束下标
# 't'
# >>> s1[2:4]
# 'th'
# >>> s1[2:6]
# 'thon'
# >>> s1[2:666]
# 'thon'
# >>> s1[2:] 到尾
# 'thon'
# >>> s1[:2] 从头
# 'py'
# >>> s1[:] 从头到尾
# 'python'
# >>> s1[::2] 2是步长值
# 'pto'
# >>> s1[1::2]
# 'yhn'
# >>> s1[::-1] 步长值为-1表示从右向左取值
# 'nohtyp'
# >>> s1[1::-1]
# 'yp'

#字符串的拼接和重复
# >>> 'abc'+'123' 拼接
# 'abc123'
# >>> '*'*5 重复'*'5遍
# '*****'
# >>> 'ab'*5 重复'ab'5遍
# 'ababababab'

#成员关系判断
# >>> s1
# 'python'
# >>> 't' in s1 字符串是否在s1中
# True
# >>> 'th' in s1
# True
# >>> 'to' not in s1 字符串是否不在s1中
# True

#列表：类似于shell中的数组
# >>> l1=['tom','jerry',10,[1,2,3]]
# >>> len(l1) 列表长度
# 4
# >>> l1[-1] 取下标
# [1, 2, 3]
# >>> l1[-1]=30 将最后一项重新赋值
# >>> l1
# ['tom', 'jerry', 10, 30]
# >>> 10 in l1 判断10是否在数组内
# True
# >>> l1[:2] 切片
# ['tom', 'jerry']
# >>> l1.append(20) 在结尾追加20
# >>> l1
# ['tom', 'jerry', 10, 30, 20]

#元组：不可变的列表
# >>> t1=('tom','jerry',10,20)
# >>> len(t1)
# 4
# >>> t1[2:]
# (10, 20)
# >>> t1[0]='bob' 报错(不可改)

#字典：没有顺序
# >>> d1={'name':'tom','age':20}
# >>> len(d1)
# 2
# >>> 'tom' in d1 'tom'是字典的键key吗？
# False
# >>> 'name' in d1
# True
# >>> d1['name'] 取出字典中name对应的值value；键值对
# 'tom'
