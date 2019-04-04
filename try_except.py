my_dict={"g":1, "r":2, "b":3}

try:
	value=my_dict["m"]
except KeyError:
	print("This key is missing!")
try:
	y=5/0
except ArithmeticError:
	print("you cannot divide by 0")
try:
	import s1 as s
except ImportError:
	print("Failed to import a module or its attribute")
