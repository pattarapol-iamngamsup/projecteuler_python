""" Copyright 2014, March 29
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Euler discovered the remarkable quadratic formula:
		n^2 + n + 41
	
	It turns out that the formula will produce 40 primes 
	for the consecutive values n = 0 to 39. However, 
	when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
	and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
	
	The incredible formula  n^2 ? 79n + 1601 was discovered, 
	which produces 80 primes for the consecutive values n = 0 to 79. 
	The product of the coefficients, ?79 and 1601, is ?126479.
	
	Considering quadratics of the form:
		n^2 + an + b, where |a| < 1000 and |b| < 1000
	
	where |n| is the modulus/absolute value of n
	e.g. |11| = 11 and |?4| = 4
	
	Find the product of the coefficients, a and b, 
	for the quadratic expression that produces the maximum number of primes 
	for consecutive values of n, starting with n = 0.
"""

#################################################
#   Importing libraries & modules
import datetime

import sys

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
	
	#	initialize max of n and coefficients
	maxN = 0
	ansA = 0
	ansB = 0
	
	#	loop a from -999 to 999
	for a in xrange( -999, 1000 ):
		#	loop b from -999 to 999
		for b in xrange( -999, 1000 ):
			#	loop n from 0 to max until not a prime number
			for n in xrange( 0, sys.maxint ):
				if not MyMathSolver.isPrimeNumber( n**2 + ( a * n ) + b ):
					break
			#	check n if more than max of n then update it and coefficients
			if n > maxN:
				maxN = n
				ansA = a
				ansB = b
	
	print( 'answer = {0}, a={1}, b={2}, maxN={3}'.format( ansA * ansB, ansA, ansB, maxN ) )

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
