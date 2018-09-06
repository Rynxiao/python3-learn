#!/usr/bin/env python3

# pickling
import pickle, json

d = dict(name = 'Bob', age = 20, score = 88)
# print(pickle.dumps(d))

with open('dump.txt', 'wb') as f:
  pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
  d = pickle.load(f)
  print(d)

# json
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

# json 进阶
class Student(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score

def student2dict(std):
  return {
    'name': std.name,
    'age': std.age,
    'score': std.score
  }

s = Student('Bob', 20, 88)
print(json.dumps(s, default = student2dict))

# 任意
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
  return Student(d['name'], d['age'], d['score'])

print(json.loads(json_str, object_hook=dict2student))

# ensure_ascii = True
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)