#coding=utf-8
def make_pizza(size,*toppings):
	"""概述要制作的pizza"""
	print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')