import os

class TicTacToe:

	def __init__(self):
		self.table = [["-","-","-"],["-","-","-"],["-","-","-"]]
		self.player = 	"X"
		self.winner = None
		self.running = True


	def _show_table(self):
		for row in self.table:
			print(row)


	def _change_player(self):
		self.player = "O" if self.player == "X" else "X"


	def _move(self):
		move_place = input(f"Enter Row & Col count to move {self.player}: ")
		row, col = move_place.split(" ")
		# checks if the table cell is blank
		if self.table[int(row)-1][int(col)-1] == "-":
			self.table[int(row)-1][int(col)-1] = self.player


	def _message(self):
		os.system('cls' if os.name=='nt' else 'clear')
		self._show_table()
		if self.winner is not None:
			print(f"{self.winner} wins!!")
		elif not self.running:
			print("Draw!!")


	def _game_check(self):
		# horizontal check
		for row in self.table:
			win = True
			for content in row:
				if content != self.player:
					win = False
					break
			if win == True:
				self.winner = self.player
				self._message()
				break

		# vertical check
		for col in range(len(self.table)):
			win = True
			for row in range(len(self.table)):
				if self.table[row][col] != self.player:
					win = False
					break
			if win == True:
				self.winner = self.player
				self._message()
				break

		# left diagonal check
		for index, row in enumerate(self.table):
			win = True
			if row[index] != self.player:
				win = False
				break
		if win == True:
			self.winner = self.player
			self._message()

		# right diagonal check
		for index, row in enumerate(self.table[::-1]):
			win = True
			if row[index] != self.player:
				win = False
				break
		if win == True:
			self.winner = self.player
			self._message()

		# blank table cells check
		blank_cells = 0
		for row in self.table:
			for cell in row:
				if cell == "-":
					blank_cells += 1
		if blank_cells == 0:
			self.running = False
			self._message()


	def main(self):
		while self.running and self.winner == None:
			os.system('cls' if os.name=='nt' else 'clear')
			self._show_table()
			self._move()
			self._game_check()
			self._change_player()


if __name__ == "__main__":
	g  = TicTacToe()
	g.main()






"""
yellow bg, orange sb, light blue instructions - In Pallette in Browser

Make it Right Phase
-replan game
	*flow
	*to add
	*frame per sec update (chars added must stay in their pos)
-draw characters
	*draw line/circle char or append img?


	
drawing the board config might be done w/:
	def _draw_cell(self, cell):
		pygame.draw.rect(screen, self.line_color, cell)

	def _make_cell(self):
		for col in range(3):
			for row in range(3):
				self._draw_cell(pygame.Rect(row * self.cell_width, col * self.cell_height, self.cell_width, self.cell_height))
		self._draw_cell()


	def draw_char(self, x, y, player):
		filled_cell = []
		for y_index, col in enumerate(self.table):
			for x_index, cell in enumerate(col):
				if cell == "X" or cell == "O":
					filled_cell.append((x_index, y_index))
		print(filled_cel)
"""