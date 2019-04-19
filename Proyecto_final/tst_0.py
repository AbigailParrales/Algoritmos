import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

matrixLike = ['dijkstra.txt','prims.txt']


def printMatrix(matrix):
	for i in range(len(matrix)):
		print (matrix[i])
	print('\n')

def txt2matrix(file):
	matrixInput = []
	matrixOutput = []

	input_var = False
	fi = open(file, "r")
	for line in fi:
		if 'Input:' in line:
			inputVar = True
			outputVar = True
		if 'Output:' in line:
			inputVar = False
			outputVar = True
		if (inputVar == True) and ('Input:' not in line):
			matrixInput.append(line.split())
		if (outputVar == True) and (inputVar == False) and ('Output:' not in line) and ('Input:' not in line):
			matrixOutput.append(line.split())
	#print('Input: ',matrixInput,'\n')
	#print('Output: ',matrixOutput,'\n')
	return matrixInput, matrixOutput
			

def readDirectory():
	Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
	directory = askdirectory() # show an "Open" dialog box and return the path to the selected file
	files = os.listdir(directory)
	for x in files:
		print(x)
		if x in matrixLike:
			mIn, mOut = txt2matrix(directory+'/'+x)
			print('Input: ','\n')
			printMatrix(mIn)
			print('Output: ','\n')
			printMatrix(mOut)
	#print(files)

#file = '"'+file_received+'"'	#Used for opening a file from py script
#fi = open(file_received, "r")

#mIn, mOut = txt2matrix('C:/Users/danie/Documents/Escuela/Universidad/6to semestre/Algoritmos/Algoritmos/Proyecto_final/text_files/prims.txt')
#print('Input: ','\n')
#printMatrix(mIn)
#rint('Output: ','\n')
#printMatrix(mOut)

readDirectory()