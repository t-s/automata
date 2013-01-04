import sys
from PIL import Image

grid = []
row = []
tempRow = []
rule = []
length = 0

#calculates cell from rule string, position of new cell, and previous row
def calcCell(ruleString,position,prevRow):
	binaryString = ""
	for pos in range(position,position+3):
		pos = pos-1
		if pos < 0:
			pos = len(prevRow)-1
		elif pos >= len(prevRow):
			pos = 0
		binaryString += str(prevRow[pos])
	return ruleString[int(binaryString,base=2)]

if (len(sys.argv) < 3):
	print 'Syntax: automata.py [initial state] [rule string] [iterations]'
	print 'The intial state should be a binary string.'
	print 'The rule string can be a binary string or a decimal up to 256.'
	print 'Using default values.'
	print ''

	row = [0,0,0,0,1,0,0,0,0]
	rule = [0,1,1,1,1,0,1,0]
	iters = 50

else:
	ruleInput = sys.argv[2]	
	for letter in sys.argv[1]:
		row.append(int(letter))
	if((len(ruleInput) > 3)):
		for bit in ruleInput:
			rule.append(int(bit))
	else:
		ruleInput = bin(int(ruleInput)).lstrip("0b") #bin() adds 0b to string
		while(len(ruleInput) < 8):
			ruleInput = "0" + str(ruleInput)
		for digit in ruleInput:
			rule.append(int(digit))
	try:
		iters = int(sys.argv[3])
	except IndexError:
		print "You did not define a number of iterations."
		print "Using default value of 50 iterations."
		iters = 50

width = len(row)
height = iters+1
img = Image.new('RGB', (width,height))

grid.append(row)
length = len(row)

for i in range(iters): #i being the number of rows in cell grid
	for j in range(length): #j being the number of cells in row
		tempRow.append(calcCell(rule,j,grid[i]))
	grid.append(tempRow)
	tempRow = []

#for eachRow in grid:
#	print eachRow

pixelGrid = []
pixelRow = []
for i in range(0,len(grid)):
	for j in range(0,len(grid[i])):
		if grid[i][j] == 1:
			pixelGrid.append((0,0,0))
		else:
			pixelGrid.append((255,255,255))

img.putdata(pixelGrid,0,0)
img = img.resize((width*15,height*15))
img.save('img.png')
img.show()
