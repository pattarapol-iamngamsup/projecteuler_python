""" Copyright 2012, August 05
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Longest Collatz sequence
	Problem 14
	
	The following iterative sequence is defined 
	for the set of positive integers:

	n -> n/2 (n is even)
	n -> 3n + 1 (n is odd)

	Using the rule above and starting with 13, 
	we generate the following sequence:

	13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
	It can be seen that this sequence (starting at 13 and finishing at 1) 
	contains 10 terms.
	
	Although it has not been proved yet (Collatz Problem),
	it is thought that all starting numbers finish at 1.

	Which starting number, under one million, produces the longest chain?
	NOTE: Once the chain starts the terms are allowed to go above one million.
"""

#################################################
#   Importing libraries & modules
import datetime

#################################################
#   Global variables

#################################################
#   Functions
def countChain(num):
	
	count = 0
	while num!=1:
		if num%2==0:
			num /= 2
		else:
			num = 3*num+1
		count += 1
	return count

#################################################
#   Classes

#################################################
#   Main function
def main():
	
	maxChain = 0
	produceNum = 0
	for i in range(1, 10**6):
		countNum = countChain(i)
		if countNum > maxChain:
			maxChain = countNum
			produceNum = i
	print( 'answer = {0}'.format( produceNum ) )

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
