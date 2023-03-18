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

	def __init__(self, cell_size):
		self.cell_size = cell_size
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
		self.font = pygame.font.SysFont("Courier New", 20)
		self.FPS = pygame.time.Clock()


	def draw_table(self):
		# draw this part w/ math
		r1 = pygame.draw.line(screen, self.table_color, [20, 150], [430, 150], 8)
		r2 = pygame.draw.line(screen, self.table_color, [20, 300], [430, 300], 8)
		c1 = pygame.draw.line(screen, self.table_color, [150, 20], [150, 430], 8)
		c2 = pygame.draw.line(screen, self.table_color, [300, 20], [300, 430], 8)
		instructions = self.font.render('Instructions here', True, (10,0,10))
		screen.blit(instructions,(125,450))


	def _change_player(self):
		self.player = "O" if self.player == "X" else "X"


	def draw_char(self, x, y, player):
		if self.player == "O":
			img = pygame.image.load("images/Tc-O.png")
		elif self.player == "X":
			img = pygame.image.load("images/Tc-X.png")
		img = pygame.transform.scale(img, (self.cell_size, self.cell_size))
		screen.blit(img, (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))


	def move(self, pos):
		x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
		if self.table[x][y] == "-":
			self.table[x][y] = self.player
			self.draw_char(x,y,self.player)


	def _message(self):
		if self.winner is not None:
			print(f"{self.winner} wins!!")
		elif not self.taking_move:
			print("Draw!!")


	def _game_check(self):
		# vertical check
		for col in self.table:
			win = True
			for content in col:
				if content != self.player:
					win = False
					break
			if win == True:
				self.winner = self.player
				self._message()
				break

		# horizontal check
		for row in range(len(self.table)):
			win = True
			for col in range(len(self.table)):
				if self.table[col][row] != self.player:
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
			self.taking_move = False
			self._message()


	def main(self):
		screen.fill(self.background_color)
		while self.running:
			self.draw_table()
			mx, my = pygame.mouse.get_pos()
			for self.event in pygame.event.get():
				if self.event.type == pygame.QUIT:
					self.running = False

				if self.event.type == pygame.MOUSEBUTTONDOWN:
					if self.taking_move:
						self.move(self.event.pos)
						self._game_check()
						self._change_player()

			pygame.display.flip()
			self.FPS.tick(60)


f = TicTacToe(cell_size)
f.main()
