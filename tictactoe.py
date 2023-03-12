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
