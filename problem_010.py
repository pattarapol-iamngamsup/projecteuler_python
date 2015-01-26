""" Copyright 2012, July 31
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Summation of primes
	Problem 10
	
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

	Find the sum of all the primes below two million.
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
	summaryPrimeNumber = 2 + 3 + 5 + 7
	for number in range( 11, 2000000, 2 ):
		if MyMathSolver.isPrimeNumber( number ):
			summaryPrimeNumber += number
	print( 'answer = {0}'.format( summaryPrimeNumber ) )
	
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
