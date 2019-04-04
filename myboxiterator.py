class MyBoxIterator:
	def __init__(self, b):
		self.b= b
		self.ind=0

	def __iter__(self):
		return self

	def __next__(self):
		if self.ind<len(self.b):
			item = self.b[self.ind]
			self.ind += 1
			return item
		else:
			raise StopIteration   
