""" Copyright 2012, August 03
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Lattice paths
	Problem 15
	
	Starting in the top left corner of a 22 grid,
	there are 6 routes (without backtracking) to the bottom right corner.
	
	How many routes are there through a 20 x 20 grid?
"""

#################################################
#   Importing libraries & modules
import datetime

#################################################
#   Global variables

#################################################
#   Functions
def generatePascalTriangle_recursive(rowNum, maxRowNum, pascalList):
	""" recursive for generate list of pascal triangle number 
		return list containing tuples of triangle numbers
	"""
	
	if rowNum == maxRowNum:
		return pascalList
	else:
		prevRow = pascalList[-1]
		nextRow = list()
		for index in range(0, len(prevRow)):
			if index+1 >= len(prevRow):
				nextRow.append(prevRow[index])
			else:
				nextRow.append(prevRow[index]+prevRow[index+1])

		nextRow.insert(0,1)
		pascalList.append(nextRow)
		return generatePascalTriangle_recursive(rowNum+1, maxRowNum, pascalList)


def generatePascalTriangle(rowNum):
	""" get pascal triangle n rows
		return list containing tuples of triangle numbers
	"""
	
	if rowNum > 0:
		initPascalList = list()
		firstRow = list()
		firstRow.append(1)
		initPascalList.append(firstRow)
		return generatePascalTriangle_recursive(1, rowNum, initPascalList)

#################################################
#   Classes

#################################################	
def main():
	print( 'answer = {0}'.format( generatePascalTriangle(41)[-1][41/2] ) )
	
#################################################
#   Main execution
if __name__ == '__main__':
	#   get starting date time
	startingDateTime = datetime.datetime.utcnow()
	print( 'startingDateTime = {0} UTC'.format( startingDateTime ) )

	#   call main function
	main()

	#   get ending date time
	endingdateTime = datetime.datetime.utcnow()
	print( 'endingdateTime = {0} UTC'.format( endingdateTime ) )

	#   compute delta date time
	deltaDateTime = endingdateTime - startingDateTime
	print( 'deltaDateTime = {0}'.format( deltaDateTime ) )
