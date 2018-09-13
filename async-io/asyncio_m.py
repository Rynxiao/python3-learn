#!/usr/bin/env python3

import asyncio
import threading

@asyncio.coroutine
def hello():
  print('Hello world! (%s)' % threading.currentThread())
  r = yield from asyncio.sleep(1)
  print('Hello again! (%s)' % threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

@asyncio.coroutine
def wget(host):
  print('wget %s...' % host)
  connect = asyncio.open_connection(host, 80)
  reader, writer = yield from connect
  header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
  writer.write(header.encode('utf-8'))
  yield from writer.drain()
  while True:
    line = yield from reader.readline()
    if line == b'\r\n':
      break
    print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
  writer.close()

loop1 = asyncio.get_event_loop()
tasks1 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop1.run_until_complete(asyncio.wait(tasks1))
loop1.close()