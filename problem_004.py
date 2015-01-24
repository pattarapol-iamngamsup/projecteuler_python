""" Copyright 2012, July 30
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Largest palindrome product
	Problem 4
	
	A palindromic number reads the same both ways.
	The largest palindrome made from
	the product of two 2-digit numbers is 9009 = 91 x 99.

	Find the largest palindrome made from the product of two 3-digit numbers.
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
	# initial
	largestPalindrome = 0
	
	# loop 2 3-digit numbers
	for i in range( 100, 1000 ):
		for j in range( 100, 1000 ):
			# product must larger than old
			if i*j > largestPalindrome:
				# is it a palindrome
				num = i*j
				if MyMathSolver.isPalindromicString( str( num ) ):
					# yes, it's, keep it
					largestPalindrome = num
	print( 'answer = {0}'.format( largestPalindrome ) )

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
