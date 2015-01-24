""" Copyright 2012, July 30
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Smallest multiple
	Problem 5
	
	2520 is the smallest number that can be divided by
	each of the numbers from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly
	divisible by all of the numbers from 1 to 20?
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
	lcm = 1
	for i in range( 2, 21 ):
		lcm = MyMathSolver.getLCM( lcm, i )
	print( 'answer = {0}'.format( lcm ) )

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
