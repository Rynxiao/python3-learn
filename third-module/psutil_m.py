#!/usr/bin/env python3

import psutil

print('统计CPU的逻辑核心数和实际核心数')
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

# 统计CPU的用户、系统、空闲时间
print('统计CPU的用户、系统、空闲时间')
print(psutil.cpu_times())

# top
print('TOP')
for x in range(10):
  print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息
print('内存信息')
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 获取磁盘信息
# 磁盘分区信息
print('磁盘分区信息')
print(psutil.disk_partitions())
# 磁盘使用情况
print('磁盘使用情况')
print(psutil.disk_usage('/'))
# 磁盘IO
print('磁盘IO')
print(psutil.disk_io_counters())

# 获取网络信息
# 获取网络读写字节/包的个数
print('获取网络读写字节/包的个数')
print(psutil.net_io_counters())
# 获取网络接口信息
print('获取网络接口信息')
print(psutil.net_if_addrs())
# 获取网络接口状态
print('获取网络接口状态')
print(psutil.net_if_stats())
# 获取当前网络连接信息
print('获取当前网络连接信息')
print(psutil.net_connections())

# 获取进程信息
print('所有进程ID')
print(psutil.pids())

# ps
print('PS')
print(psutil.test())




