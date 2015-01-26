""" Copyright 2014, April 3
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Sub-string divisibility
	Problem 43
	
	The number, 1406357289, is a 0 to 9 pandigital number because 
	it is made up of each of the digits 0 to 9 in some order, 
	but it also has a rather interesting sub-string divisibility property.
	
	Let d1 be the 1st digit, d2 be the 2nd digit, and so on. 
	In this way, we note the following:
	
	d2d3d4=406 is divisible by 2
	d3d4d5=063 is divisible by 3
	d4d5d6=635 is divisible by 5
	d5d6d7=357 is divisible by 7
	d6d7d8=572 is divisible by 11
	d7d8d9=728 is divisible by 13
	d8d9d10=289 is divisible by 17
	
	Find the sum of all 0 to 9 pandigital numbers with this property.
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
	
	answer = 0
	for index in xrange( 0, MyMathSolver.getFactorialValue( 10 ) ):
		numStr = MyMathSolver.getPermutationString( range( 0, 10 ), index )
		if int( numStr[1:4] ) % 2 == 0:
			if int( numStr[2:5] ) % 3 == 0:
				if int( numStr[3:6] ) % 5 == 0:
					if int( numStr[4:7] ) % 7 == 0:
						if int( numStr[5:8] ) % 11 == 0:
							if int( numStr[6:9] ) % 13 == 0:
								if int( numStr[7:10] ) % 17 == 0:
									answer += int( numStr )
	print( 'answer = {0}'.format( answer ) )

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
