""" Copyright 2012, August 07
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Factorial digit sum
	Problem 20
	
	n! means n x (n - 1) x ... x 3 x 2 x 1
	
	For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
	and the sum of the digits in the number 10! 
	is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
	
	Find the sum of the digits in the number 100!
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
	product = 1
	for i in range( 2, 101 ):
		product *= i
	
	summary = 0
	for numberChar in str( product ):
		summary += int( numberChar )
	print( 'answer = {0}'.format( summary ) )
	
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
