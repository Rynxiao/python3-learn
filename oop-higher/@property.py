#!/usr/bin/env python3

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value	

	@property
	def age(self):
		return 2018 - self._birth
	

s = Student()
s.score = 60
print(s.score)

# ValueError: score must between 0 ~ 100!
# s.score = 9999

s.birth = 1991
print(s.age)

# AttributeError: can't set attribute
# s.age = 29

class Screen(object):

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

	
	
	




	
	