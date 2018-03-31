#draw_grid.py
def draw_grid(row, col):


	def plus_line():
		for i in range(col):
			print("+", end = " ")
			for i in range(4):
				print("-", end = " ")
		print("+")


	def or_space():
		for i in range(4):
			for k in range(col):
				print("|", end = " ")
				for i in range(4):
					print(" ", end = " ")
			print("|")


	for i in range(row):
		plus_line()
		or_space()
	plus_line()


while True:
        try:
                dimension = input("Enter <ROW> comma <COLUMN>: " ).split(",")
                dim = list(map(int, dimension))

                for i in dim:
                        assert 0 < i <= 10

                draw_grid(dim[0], dim[1])

                break

        except (ValueError, AssertionError, IndexError):
                print("INVALID INPUT!!! ENTER NUMBER OF ROWS AND COLUMNS BTW 0 AND 11")
                

        

