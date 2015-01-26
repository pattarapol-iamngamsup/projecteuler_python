""" Copyright 2012, August 08
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Names scores
	Problem 22
	
	Using names.txt (right click and 'Save Link/Target As...'),
	a 46K text file containing over five-thousand first names,
	begin by sorting it into alphabetical order.
	Then working out the alphabetical value for each name,
	multiply this value by its alphabetical position in the list
	to obtain a name score.

	For example, when the list is sorted into alphabetical order,
	COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
	is the 938th name in the list.
	So, COLIN would obtain a score of 938  53 = 49714.

	What is the total of all the name scores in the file?
"""
#################################################
#   Importing libraries & modules
import datetime

import csv

#################################################
#   Global variables

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function
def main():
	offset = ord('A') - 1
	print( 'offset = {0}'.format( offset ) )
	
	with open( 'problem_022.txt', 'rb' ) as openedFile:
		csvReader = csv.reader( openedFile )
		nameList = csvReader.next()
		nameList.sort()
		order = 1
		sumScore = 0
		for name in nameList:
			score = 0
			for char in name:
				score += ord( char.upper() ) - offset
			score *= order
			sumScore += score
			order += 1
		print( 'answer = {0}'.format( sumScore ) )
	
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
