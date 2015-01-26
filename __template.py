""" Copyright 2014, March 14
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	OBJECTIVES HERE
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
	pass

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
