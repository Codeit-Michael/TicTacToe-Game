horizontal check
tb = [["-","-","-"],["X","X","X"],["-","-","-"]]

player = "X"

for x in tb:
	win = True
	for y in x:
		if y != player:
			win = False
	if win == True:
		break
print(win, x, y)


# vertical check
tb = [["-","X","-"],["-","X","-"],["-","X","-"]]

player = "X"

for index, x in enumerate(tb):
	win = True
	for y in range(len(tb)):
		print(tb[y][index])
		if tb[y][index] != player:
			win = False
	if win == True:
		break
print(win)


left diagonal check
tb = [["X","-","-"],["-","X","-"],["-","-","X"]]

player = "X"

for index, x in enumerate(tb):
	win = True
	if x[index] != player:
		win = False
		break
print(win)


right diagonal check
tb = [["-","-","X"],["-","X","-"],["X","-","-"]]

player = "X"

for index, x in enumerate(tb[::-1]):
	win = True
	if x[index] != player:
		win = False
		break
print(win)