#!/usr/bin/env python3

import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
print(os.uname)

# 环境变量
print(os.environ)
print(os.environ.get('PATH'))

# 文件和目录
print(os.path.abspath('.'))
# 创建新目录
folderPath = os.path.join(os.path.abspath('.'), 'testdir')
os.mkdir(folderPath)

# 删除目录
# os.rmdir(folderPath)

# 拆分路径
print(os.path.split('/Users/yhhu/tsetdir/file.txt'))

# 得到后缀
print(os.path.splitext('/path/to/file.txt'))

# 重命名
os.rename('test.txt', 'test.py')

# 删除文件
# os.remove('test.py)

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])


