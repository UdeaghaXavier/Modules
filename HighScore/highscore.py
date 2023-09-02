class highscore:
	def __init__(self, file, score):
		""" __init__

		Args:
			file ([string]): [directory to the txt file] \n
			score ([string]): [score]
		"""
  
		self.file = file
		self.score = score
 
	def read_file(self):
		with open(self.file, 'r') as File:
			data = File.read()
		return data

	def write_to_file(self, data = ''):
		with open(self.file, 'w') as File:
			File.write(data)

	def clear_file(self):
		self.write_to_file()

	def main(self):
		# Only store the score in the given txt file if the score given is greater
		# than the value currently in the txt file, if the file was originally empty 
		# store the value without checking
		data = self.read_file()
		if data:
			if self.n > int(data):
				self.write_to_file(str(self.score))
			return
		self.write_to_file(str(self.score))
		