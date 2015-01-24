""" Copyright 2012, July 29
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Multiples of 3 and 5
	Problem 1
	
	If we list all the natural numbers below 10 
	that are multiples of 3 or 5, we get 3, 5, 6 and 9.
	The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.
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
	""" space is natural number below 1000
		event is multiples of given number
		each event are independent thus members may exist
		so use set theory A+B-(AB) 
	"""
	# compute sum of all the multiples of given number
	sum3 = (999/3)**2 + 999/3
	sum5 = (999/5)**2 + 999/5
	sum15 = (999/15)**2 + 999/15
	print( 'answer = {0}'.format( 3*sum3/2 + 5*sum5/2 - 15*sum15/2 ) )

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
