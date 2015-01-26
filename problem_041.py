""" Copyright 2014, March 21
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Pandigital prime
	Problem 41
	
	We shall say that an n-digit number is pandigital 
	if it makes use of all the digits 1 to n exactly once.
	
	For example, 2143 is a 4-digit pandigital and is also prime.
	
	What is the largest n-digit pandigital prime that exists?
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
	
	largestPanDigitalPrimeNumber = 2
	for digitNumber in xrange( 1, 10 ):
		for panDigitalNumber in MyMathSolver.getPanDigitalNumbersList( digitNumber ):
			if MyMathSolver.isPrimeNumber( panDigitalNumber ):
				largestPanDigitalPrimeNumber = panDigitalNumber
				print( 'answer = {0}'.format( largestPanDigitalPrimeNumber ) )

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
