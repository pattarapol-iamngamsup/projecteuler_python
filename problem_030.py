""" Copyright 2014, March 14
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Digit fifth powers
	Problem 30
	
	Surprisingly there are only three numbers that can be written as 
	the sum of fourth 
	
	powers of their digits:
	
	1634 = 14 + 64 + 34 + 44
	8208 = 84 + 24 + 04 + 84
	9474 = 94 + 44 + 74 + 44
	As 1 = 14 is not a sum it is not included.
	
	The sum of these numbers is 1634 + 8208 + 9474 = 19316.
	
	Find the sum of all the numbers that can be written as 
	the sum of fifth powers of their digits.
"""

#################################################
#   Importing libraries & modules
import datetime

#################################################
#   Global variables

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function
def main():
	
	matchNumsList = []
	powerNum = 5
	maxDigitPowerNum = 9 ** powerNum
	for num in xrange( 10, maxDigitPowerNum * powerNum ):
		numStr = str( num )
		sumDigitPowersNum = 0
		for numChar in numStr:
			sumDigitPowersNum += int( numChar ) ** powerNum
		if sumDigitPowersNum == num:
			matchNumsList.append( num )
			print( 'num = {0}'.format( num ) )
	print( 'answer = {0}'.format( sum( matchNumsList ) ) )
	
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
