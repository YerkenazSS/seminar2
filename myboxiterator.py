class MyBoxIterator():
	def __init__(self):
		self.b = 1

	def __iter__(self):
		return self

	def __next__(self):
		if self.b <= 5:
			c = self.b
			self.b += 1
			return c
		else:
			raise StopIteration
if __name__ == "__main__":
	L = MyBoxIterator()
	for item in L:
		print(item)     
