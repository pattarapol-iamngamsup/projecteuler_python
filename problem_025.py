""" Copyright 2014, March 27
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	1000-digit Fibonacci number
	Problem 25
	
	What is the first term in the Fibonacci sequence to contain 1000 digits?
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
	
	f = m = n = 1
	counter = 2
	while True:
		f = m + n
		#print( '{0}, {1}, {2}'.format( m, n, f ) )
		tmp = n
		m = tmp
		n = f
		counter += 1
		if f >= 10**999:
			print( 'answer = {0}'.format( counter ) )
			break

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
