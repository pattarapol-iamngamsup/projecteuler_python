""" Copyright 2014, March 29
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Distinct powers
	Problem 29
	
	Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:
	
	2^2=4, 2^3=8, 2^4=16, 2^5=32
	3^2=9, 3^3=27, 3^4=81, 3^5=243
	4^2=16, 4^3=64, 4^4=256, 4^5=1024
	5^2=25, 5^3=125, 5^4=625, 5^5=3125
	
	If they are then placed in numerical order, with any repeats removed, 
	we get the following sequence of 15 distinct terms:
	
	4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
	
	How many distinct terms are in the sequence generated by a^b 
	for 2 <= a <= 100 and 2 <= b <= 100?
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
	
	distinctsSet = set()
	for a in xrange( 2, 101 ):
		for b in xrange( 2, 101 ):
			distinctsSet.add( a**b )
	print( 'answer = {0}'.format( len( distinctsSet ) ) )

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
