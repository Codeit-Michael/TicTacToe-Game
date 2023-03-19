import os

import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

window_size = (450, 500)
cell_size = 150

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe")


class TicTacToe():

	def __init__(self, cell_size, table_length):
		self.cell_size = cell_size
		self.table_length = table_length
		self.table_space = 20

		self.player = "X"
		self.winner = None
		self.taking_move = True
		self.running = True
		self.table = []
		for col in range(3):
			self.table.append([])
			for row in range(3):
				self.table[col].append("-")

		self.background_color = (200, 200, 230)
		self.table_color = (10, 20, 7)
		self.line_color = (190, 0, 10)
		self.game_over_color = (0, 0, 79)
		self.font = pygame.font.SysFont("Courier New", 35)
		self.FPS = pygame.time.Clock()


	def _change_player(self):
		self.player = "O" if self.player == "X" else "X"


	def _draw_table(self):
		tb_space_point = (self.table_space, self.table_length - self.table_space)
		cell_space_point = (self.cell_size, self.cell_size * 2)
		r1 = pygame.draw.line(screen, self.table_color, [tb_space_point[0], cell_space_point[0]], [tb_space_point[1], cell_space_point[0]], 8)
		c1 = pygame.draw.line(screen, self.table_color, [cell_space_point[0], tb_space_point[0]], [cell_space_point[0], tb_space_point[1]], 8)
		r2 = pygame.draw.line(screen, self.table_color, [tb_space_point[0], cell_space_point[1]], [tb_space_point[1], cell_space_point[1]], 8)
		c2 = pygame.draw.line(screen, self.table_color, [cell_space_point[1], tb_space_point[0]], [cell_space_point[1], tb_space_point[1]], 8)


	def _draw_char(self, x, y, player):
		if self.player == "O":
			img = pygame.image.load("images/Tc-O.png")
		elif self.player == "X":
			img = pygame.image.load("images/Tc-X.png")
		img = pygame.transform.scale(img, (self.cell_size, self.cell_size))
		screen.blit(img, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))


	def _pattern_strike(self, x, y):
		val = self.cell_size // 2
		start_x, start_y = x[0] * self.cell_size + self.table_space, x[-1] * self.cell_size + val
		end_x, end_y = y[0] * self.cell_size + self.table_space, y[-1] * self.cell_size + val
		print([start_x, start_y], [end_x, end_y])
		pygame.draw.line(screen, self.line_color, [start_x, start_y], [end_x, end_y], 20)
		# pygame.draw.line(screen, self.line_color, [20, 75], [430, 75], 20)
		# plan this:
		# getting each cell using pattern_list
		# get each cell's center
		# create a line with those centers


	def _move(self, pos):
		x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
		if self.table[x][y] == "-":
			self.table[x][y] = self.player
			self._draw_char(x,y,self.player)
			self._game_check()
			self._change_player()	


	def _message(self):
		if self.winner is not None:
			screen.fill(self.game_over_color, (130, 440, 193, 35))
			msg = self.font.render(f'{self.winner} WINS!!', True, (10,0,10))
			screen.blit(msg,(144,440))
		elif not self.taking_move:
			screen.fill(self.game_over_color, (130, 440, 193, 35))
			instructions = self.font.render('DRAW!!', True, (10,0,10))
			screen.blit(instructions,(165,440))
		else:
			screen.fill(self.background_color, (135, 445, 188, 25))
			instructions = self.font.render(f'{self.player} to move', True, (10,0,10))
			screen.blit(instructions,(135,440))

	def _game_check(self):
		# vertical check
		for x_index, col in enumerate(self.table):
			win = True
			pattern_list = []
			for y_index, content in enumerate(col):
				if content != self.player:
					win = False
					break
				else:
					pattern_list.append((x_index, y_index))
			if win == True:
				self._pattern_strike(pattern_list[0],pattern_list[-1])
				self.winner = self.player
				self.taking_move = False
				self._message()
				break

		# horizontal check
		for row in range(len(self.table)):
			win = True
			pattern_list = []
			for col in range(len(self.table)):
				if self.table[col][row] != self.player:
					win = False
					break
				else:
					pattern_list.append((col, row))
			if win == True:
				print(pattern_list[0],pattern_list[-1])
				self._pattern_strike(pattern_list[0],pattern_list[-1])
				self.winner = self.player
				self.taking_move = False
				self._message()
				break

		# left diagonal check
		for index, row in enumerate(self.table):
			win = True
			if row[index] != self.player:
				win = False
				break
		if win == True:
			self._pattern_strike((0,0),(2,2))
			self.winner = self.player
			self.taking_move = False
			self._message()

		# right diagonal check
		for index, row in enumerate(self.table[::-1]):
			win = True
			if row[index] != self.player:
				win = False
				break
		if win == True:
			self._pattern_strike((2,0),(0,2))
			self.winner = self.player
			self.taking_move = False
			self._message()

		# blank table cells check
		blank_cells = 0
		for row in self.table:
			for cell in row:
				if cell == "-":
					blank_cells += 1
		if blank_cells == 0:
			self.taking_move = False
			self._message()


	def main(self):
		screen.fill(self.background_color)
		self._draw_table()
		while self.running:
			self._message()
			for self.event in pygame.event.get():
				if self.event.type == pygame.QUIT:
					self.running = False

				if self.event.type == pygame.MOUSEBUTTONDOWN:
					if self.taking_move:
						self._move(self.event.pos)

			pygame.display.flip()
			self.FPS.tick(60)



if __name__ == "__main__":
	g = TicTacToe(cell_size, window_size[0])
	g.main()
