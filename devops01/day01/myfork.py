#!/usr/local/bin/python3
import os

print('starting')

rc=os.fork()

if rc:  #返回值是一个数字,非0为真,0为假
    print('父进程')
else:
    print('子进程')

print('Hello World!')