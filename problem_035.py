""" Copyright 2014, March 14
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Circular primes
	Problem 35
	
	The number, 197, is called a circular prime because all rotations of 
	the digits: 197, 971, and 719, are themselves prime.
	
	There are thirteen such primes below 100: 
	2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
	
	How many circular primes are there below one million?
"""

#################################################
#   Importing libraries & modules
import datetime

from MyMathSolver import MyMathSolver

#################################################
#   Global variables
MaxNumber = 10 ** 6

#################################################
#   Functions
def countNumberDigit( number ):
	""" Count digit count given number
	"""
	
	digitCount = 1
	while number > 10**digitCount:
		digitCount += 1
	return digitCount	

#################################################
#   Classes

#################################################
#   Main function
def main():
	
	#	initialize circular prime counter
	circularPrimeCounter = 0
	
	#	initialize number list
	primeList = [ 2 ]
	primeList.extend( ( number for number in range( 3, MaxNumber + 1, 2 ) 
					if MyMathSolver.isPrimeNumber( number ) ) )
	
	#	loop over all remaining numbers
	remainingNumberCount = len( primeList )
	while remainingNumberCount:
		
		prime = primeList[0]
		primeList.remove( prime )
		remainingNumberCount -= 1
		#print prime, circularPrimeCounter, remainingNumberCount

		#	to check circular
		
		#	1. count number digit
		digitCount = countNumberDigit( prime )
		
		#	2. start rotating digit
		rotatedNumberList = []
		
		rotatedNumber = prime
		rotatingCount = 0
		while rotatingCount < digitCount - 1:
			divider = 10**( digitCount - 1 )
			dividend = int( rotatedNumber / divider )
			rotatedNumber = ( rotatedNumber - dividend * divider ) * 10 + dividend
			if rotatedNumber == prime:
				break
			
			rotatedNumberList.append( rotatedNumber )
			rotatingCount += 1
		rotatedNumberList.sort()
		
		#	3. is digit rotated number a  prime ?
		haveInvalidPrime = False
		for rotatedNumber in rotatedNumberList:
			if not haveInvalidPrime:
				if not rotatedNumber in primeList:
					haveInvalidPrime = True
			
			try:
				primeList.remove( rotatedNumber )
			except ValueError:
				pass
			else:
				remainingNumberCount -= 1
			
		if not haveInvalidPrime:
			circularPrimeCounter += rotatingCount + 1
				
	print( 'answer = {0}'.format( circularPrimeCounter ) )

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
