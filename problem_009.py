""" Copyright 2012, July 31
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Special Pythagorean triplet
	Problem 9
	
	A Pythagorean triplet is a set of three natural numbers, a  b  c,
	for which, a^2 + b^2 = c^2
	For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc.
"""

#################################################
#   Importing libraries & modules
import datetime

#################################################
#   Global variables
PythagoreanSum = 1000

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function
def main():
	for a in range (0, PythagoreanSum):
		for b in range(a+1, PythagoreanSum-a ):
			c = PythagoreanSum-a-b
			if c > b:
				if a**2 + b**2 == c**2:
					print( 'answer = {0}'.format( a * b * c ) )

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
