#!/usr/bin/env python3

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class RunnableMixIn(object):
	def run(self):
		print('Running...')

class FlyableMixIn(object):
	def fly(self):
		print('Flying...')

class Dog(Mammal, RunnableMixIn):
	pass

class Bat(Mammal, RunnableMixIn):
	pass

class Parrot(Bird, FlyableMixIn):
	pass

class Ostrich(Bird, FlyableMixIn):
	pass

d = Dog()
p = Parrot()

print(d.run())
print(p.fly())