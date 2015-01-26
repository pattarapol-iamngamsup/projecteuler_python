""" Copyright 2012, August 07
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Maximum path sum II
	Problem 67
	
	By starting at the top of the triangle below
	and moving to adjacent numbers on the row below,
	the maximum total from top to bottom is 23.

	3
	7 4
	2 4 6
	8 5 9 3

	That is, 3 + 7 + 4 + 9 = 23.

	Find the maximum total from top to bottom in triangle.txt

	NOTE: This is a much more difficult version of Problem 18.
	It is not possible to try every route to solve this problem,
	as there are 299 altogether!
	If you could check one trillion (1012) routes every second
	it would take over twenty billion years to check them all.
	There is an efficient algorithm to solve it. ;o)
"""

#################################################
#   Importing libraries & modules
import datetime

from problem_018 import getAnswer

#################################################
#   Global variables
InputFilePath = 'problem_067.txt'

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function
def main():
	
	print( 'answer = {0}'.format( getAnswer( InputFilePath ) ) )

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
