from AnyBaseConverter import Converter

if __name__ == '__main__':
	conv = Converter()

	num = int(input("Number in base 10 to convert > "))
	base = int(input("Base to convert into > "))

	print(conv.calculate(num,base))
	