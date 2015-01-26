""" Copyright 2014, March 21
	Written by Pattarapol (Cheer) Iamngamsup
	E-mail:  IAM.PATTARAPOL@GMAIL.COM
	
	Coded triangle numbers
	Problem 42
	
	The nth term of the sequence of triangle numbers is given by, 
	tn = 1/2 x n(n+1); so the first ten triangle numbers are:
		1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

	By converting each letter in a word to a number corresponding to 
	its alphabetical position and adding these values we form a word value.
	
	For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
	If the word value is a triangle number 
	then we shall call the word a triangle word.

	Using words.txt (right click and 'Save Link/Target As...'),
	a 16K text file containing nearly two-thousand common English words,
	how many are triangle words?
"""

#################################################
#   Importing libraries & modules
import datetime

import csv

#################################################
#   Global variables

InputFilePath = 'problem_042.txt'

AlphabetToValue = {}
offsetValue = 64
for value in xrange( 1, 27 ):
	AlphabetToValue[ chr( value + offsetValue ) ] = value
print( 'AlphabetToValue = {0}'.format( AlphabetToValue ) )

MinTriangleNumberIndex = 1
MaxTriangleNumberIndex = 100
TriangleNumbersList = [ ( index * ( index + 1 ) ) / 2 
						for index in xrange( MinTriangleNumberIndex, 
											MaxTriangleNumberIndex+1 ) ]
print( 'TriangleNumbersList = {0}'.format( TriangleNumbersList ) )

#################################################
#   Functions

#################################################
#   Classes

#################################################
#   Main function
def main():
	
	#   initialize triangle words counter as zero
	triangleWordsCounter = 0
	
	#   read input file, CSV format
	with open( InputFilePath, 'rb' ) as csvfile:
		#   initialize csv reader
		csvReader = csv.reader( csvfile, delimiter=',', quotechar='"' )
		#   loop over all lines
		for line in csvReader:
			#   loop over all words in a line
			for word in line:
				#   initialize word value
				wordValue = 0
				#   loop over all alphabets in a word
				for alphabet in word:
					#   increment word value					
					wordValue += AlphabetToValue[ alphabet ]
				#   check word is a triangle word then increment counter by one
				if wordValue in TriangleNumbersList:
					triangleWordsCounter += 1

	print( 'answer = {0}'.format( triangleWordsCounter ) )
	
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
