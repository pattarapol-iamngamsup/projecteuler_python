""" Copyright 2014, March 18
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Lexicographic permutations
	Problem 24

	A permutation is an ordered arrangement of objects.
	For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
	If all of the permutations are listed numerically or alphabetically,
	we call it lexicographic order.
	The lexicographic permutations of 0, 1 and 2 are: 
		012   021   102   120   201   210

	What is the millionth lexicographic permutation of the digits 
	0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

#################################################
#   Importing libraries & modules
import datetime

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
	
	values = range( 0, 10 )
	index = 10**6
	answer = MyMathSolver.getPermutationString( values, index-1 )
	print( 'answer = {0}'.format( answer ) )

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
