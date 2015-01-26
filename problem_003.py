""" Copyright 2012, July 30
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Largest prime factor
	Problem 3
	
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
"""

#################################################
#   Importing libraries & modules
import datetime

from MyMathSolver import MyMathSolver

#################################################
#   Global variables
Number = 600851475143

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function
def main():
	
	# initial largest prime
	largestPrime = None
	
	for num in range( 3, int( Number ** 0.5 ) + 1, 2 ):
		# is divided
		if Number % num == 0:
			# is prime
			if MyMathSolver.isPrimeNumber( num ):
				largestPrime = num
	print( 'answer = {0}'.format( largestPrime ) )

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
