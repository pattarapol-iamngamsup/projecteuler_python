""" Copyright 2014, March 21
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Double-base palindromes
	Problem 36

	The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
	Find the sum of all numbers, 
	less than one million, which are palindromic in base 10 and base 2.
	
	(Please note that the palindromic number, 
	in either base, may not include leading zeros.)
"""

#################################################
#   Importing libraries & modules
import datetime

from MyMathSolver import MyMathSolver

#################################################
#   Global variables
MinNum = 0
MaxNum = 10**6

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function
def main():

	#   initialize sum of palindromic number as zero
	sumPalindromicNum = 0
	
	#   loop over all numbers from min to max
	for num in xrange( MinNum, MaxNum ):
		#   check decimnal
		if MyMathSolver.isPalindromicString( str( num ) ):
			#   check binary
			binaryNumStr = bin( num )
			binaryStr = binaryNumStr.split( 'b' )[1]
			if MyMathSolver.isPalindromicString( binaryStr ):
				sumPalindromicNum += num
	
	print( 'answer = {0}'.format( sumPalindromicNum ) )

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
