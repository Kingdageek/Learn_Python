#chess_grid.py
def grid():


	def plus_line():
		for i in range(8):
			print("+", end = " ")
			for i in range(4):
				print("-", end = " ")
		print("+")


	def or_space():
		for i in range(4):
			for k in range(8):
				print("|", end = " ")
				for i in range(4):
					print(" ", end = " ")
			print("|")


	for i in range(8):
		plus_line()
		or_space()
	plus_line()


grid()

