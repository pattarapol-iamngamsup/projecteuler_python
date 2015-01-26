""" Copyright 2014, March 29
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Number spiral diagonals
	Problem 28
	
	Starting with the number 1 and moving to the right 
	in a clockwise direction a 5 by 5 
	
	spiral is formed as follows:
	
	21 22 23 24 25
	20  7  8  9 10
	19  6  1  2 11
	18  5  4  3 12
	17 16 15 14 13
	
	It can be verified that the sum of the numbers on the diagonals is 101.
	
	What is the sum of the numbers on the diagonals in a 1001 by 1001 
	spiral formed in the same way?
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
	
	size = 1001
	maxValue = size**2
	values = [ 1 ]
	index = 1
	level = 1
	c = 0
	
	while True:
		value = ( 2 * level * index ) + 1 - ( 8 * c )
		if value > maxValue:
			break
		values.append( value )
		index += 1
		if index % 4 == 1:
			c += level
			level += 1
	
	print( 'answer = {0}'.format( sum( values ) ) )
	
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
