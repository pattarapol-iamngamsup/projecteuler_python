""" Copyright 2014, March 21
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Champernowne's constant
	Problem 40
	
	An irrational decimal fraction is created by concatenating the positive integers:
		0.123456789101112131415161718192021...

	It can be seen that the 12th digit of the fractional part is 1.
	If dn represents the nth digit of the fractional part, find the value of the following expression.
		d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
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
	
	fractionString = ''
	counter = 0
	while True:
		counter += 1
		fractionString += str( counter )
		if len( fractionString ) >= 10**6:
			break

	ans = 1
	for i in xrange( 0, 7 ):
		index = ( 1 * 10**i ) - 1
		ans *= int( fractionString[ index ] )
	print( 'answer = {0}'.format( ans ) )

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
