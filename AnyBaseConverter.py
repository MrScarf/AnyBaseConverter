class Converter():
	def __init__(self):
		self.alpha = [chr(k) for k in range(65,91)] #Set an array of chars going to the letter A to the Z

	def calculate(self, seq, b):
		if not 2 <= b <= 36: #Bases range is [2,36]
			return None
		else:
			out = []
			sequence = seq
			base = b
			itr = 0 #Keep track of the number of iterations
			while sequence != 0 and itr <= 1000: 
				rem = sequence % b
				quo = sequence // b
				sequence = quo
				if rem < 10:
					out.append(str(rem))
				else:
					out.append(self.alpha[rem - 10])
				itr += 1

			out.reverse()
		return "".join(out)



