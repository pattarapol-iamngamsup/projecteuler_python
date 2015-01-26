""" Copyright 2012, August 05
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Counting Sundays
	Problem 19
	
	You are given the following information,
	but you may prefer to do some research for yourself.

	1 Jan 1900 was a Monday.
	Thirty days has September, April, June and November.
	
	All the rest have thirty-one, Saving February alone,
	Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
	
	A leap year occurs on any year evenly divisible by 4,
	but not on a century unless it is divisible by 400.
	
	How many Sundays fell on the first of the month 
	during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
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
	
	count = 0
	for year in range( 1901, 2001 ):
		for month in range( 1, 13 ):
			if datetime.datetime( year, month, 1 ).weekday() == 6:
				count += 1
	print( 'answer = {0}'.format( count ) )
	
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
