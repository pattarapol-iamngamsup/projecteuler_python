""" Copyright 2012, July 31
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Sum square difference
	Problem 6
	The sum of the squares of the first ten natural numbers is,
	1^2 + 2^2 + ... + 10^2 = 385
	
	The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)^2 = 55^2 = 3025
	
	Hence the difference between the sum of the squares of
	the first ten natural numbers and the square of the sum is
	3025  385 = 2640.

	Find the difference between the sum of the squares of
	the first one hundred natural numbers and the square of the sum.
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
	squareOfSum = ( ( ( 1+100 ) * 100 ) / 2)**2
	sumOfSquare = 0
	for i in range( 1, 101 ):
		sumOfSquare += i*i
	print( 'answer = {0}'.format( squareOfSum - sumOfSquare ) )

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
