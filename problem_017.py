""" Copyright 2012, August 05
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Number letter counts
	Problem 17
	
	If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
	then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

	If all the numbers from 1 to 1000 (one thousand) 
	inclusive were written out in words, 
	how many letters would be used?

	NOTE: Do not count spaces or hyphens. 
	For example, 
	342 (three hundred and forty-two) contains 23 letters 
	and 115 (one hundred and fifteen) contains 20 letters. 
	
	The use of "and" when writing out numbers 
	is in compliance with British usage.
"""

#################################################
#   Importing libraries & modules
import datetime

from MyMathSolver import MyMathSolver

#################################################
#   Global variables

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function


def main():
	letterCounter = 0
	for i in range(1, 1+(10**3)):
		numStr = MyMathSolver.getSpellingNumberString(i)
		numStr = numStr.replace( '-', '' )
		numStrList = numStr.split()
		for numStr in numStrList:
			letterCounter += len( numStr.strip() )
	print( 'answer = {0}'.format( letterCounter ) )
	
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
