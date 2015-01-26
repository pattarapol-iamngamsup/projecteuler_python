""" Copyright 2012, August 07
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Amicable numbers
	Problem 21
	
	Let d(n) be defined as the sum of proper divisors of n
	(numbers less than n which divide evenly into n).
	
	If d(a) = b and d(b) = a, where a != b,
	then a and b are an amicable pair 
	and each of a and b are called amicable numbers.

	For example, the proper divisors of 220 
	are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
	
	The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
	
	Evaluate the sum of all the amicable numbers under 10000.
"""

#################################################
#   Importing libraries & modules
import datetime

#################################################
#   Global variables

#################################################
#   Functions
def d( n ):
	
	divisorList = list()
	limiter = n
	i = 1
	summary = 0
	while i < limiter:
		#print 'divisorList', n, divisorList
		if n%i==0:
			limiter = n / i
			divisorList.append(i)
			summary += i
			if limiter != n and limiter != i:
				divisorList.append(limiter)
				summary += limiter
		i+=1
	
	#print 'divisorList', divisorList
	#print n, sum
	return summary

#################################################
#   Classes

#################################################
#   Main function
def main():
	summary = 0
	amicable = list()
	for a in range( 2, 10**4 ):
		b = d( a )
		if a != b:
			if a == d(b):
				if not ( a, b ) in amicable and not ( b, a ) in amicable:
					amicable.append( ( a, b ) )
					summary += a + b
	print( 'answer = {0}'.format( summary ) )

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
