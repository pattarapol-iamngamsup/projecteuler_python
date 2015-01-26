""" Copyright 2012, August 08
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Non-abundant sums
	Problem 23
	
	A perfect number is a number for which 
	the sum of its proper divisors is exactly equal to the number.
	
	For example, the sum of the proper divisors of 28 
	would be 1 + 2 + 4 + 7 + 14 = 28, 
	which means that 28 is a perfect number.

	A number n is called deficient 
	if the sum of its proper divisors is less than n
	and it is called abundant if this sum exceeds n.

	As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
	the smallest number that can be written as 
	the sum of two abundant numbers is 24.

	By mathematical analysis, 
	it can be shown that all integers greater than 28123
	can be written as the sum of two abundant numbers.

	However, this upper limit cannot be reduced any further by analysis 
	even though it is known that the greatest number that cannot be expressed 
	as the sum of two abundant numbers is less than this limit.

	Find the sum of all the positive integers which cannot be written 
	as the sum of two abundant numbers.
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
def getSumProperDivisors(n):
	sumProper = 0
	squareRootN = n**0.5
	for i in range(1, int( squareRootN )+1):
		if n%i==0:
			sumProper += i
			x = n/i
			if x!=n and x!= squareRootN:
				sumProper += x
	return sumProper


def isAbundantSum( n, abundants):
	
	for abundant in abundants:
		if n - abundant in abundants:
			return True
	return False


def main():
	limitNum = 28124
	abundants = set( 
		n for n in range( 1, limitNum ) 
			if getSumProperDivisors( n ) > n 
	)
	print( 'answer = {0}'.format( sum( n for n in range( 1, limitNum ) 
									if not isAbundantSum( n, abundants ) ) ) )
	
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
