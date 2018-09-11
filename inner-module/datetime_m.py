#!/usr/bin/env python3

import re
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)
print(dt)
print(dt.timestamp())

t = 1429417200.0
# 北京时间
print(datetime.fromtimestamp(t))
# 格林威治时间
print(datetime.utcfromtimestamp(t))

# str -> datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime -> str
now1 = datetime.now()
print(now1.strftime('%a, %b %d %H:%M'))

# datetime 加减
now2 = datetime.now()
print(now2)
print(now2 + timedelta(hours=10))
print(now2 - timedelta(days=1))
print(now2 + timedelta(days= 2, hours=12))

# 本地时间转换为UTC时间
tz_utc_8 = timezone(timedelta(hours=8))
now3 = datetime.now()
print(now3)
dt = now3.replace(tzinfo=tz_utc_8)
print(dt)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

def to_timestamp(dt_str, tz_str):
  g = re.match(r'UTC(\+|-)(\d+?):00', tz_str).groups()
  hours = int(g[0] + g[1])
  tz_utc = timezone(timedelta(hours=hours))
  dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=tz_utc)
  return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')