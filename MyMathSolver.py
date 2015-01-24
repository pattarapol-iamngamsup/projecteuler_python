#
#   Copyright 2011 - Present
#   Written by Pattarapol (Cheer) Iamngamsup
#   E-mail:  IAM.PATTARAPOL@GMAIL.COM
#

#################################################
#   Importing libraries & modules
import sys

import math

import fractions

#################################################
#   Global variables

#################################################
#   Functions

#################################################
#   Classes
class MyMathSolver( object ):
	""" My math solver class.
	"""
	
	@staticmethod
	def getPermutationString( values, index ):
		""" Get the permutation value string at given index.
		
			Notes:	Index starts counting from zero.
		"""
		
		""" Find 20th permutation value of given values
			 
			E = values = [ 0, 1, 2, 3 ]
			S = { 
				0123, 0132, 0213, 0231, 0312, 0321
				1023, 1032, 1203, 1230, 1302, 1320
				2013, 2031, 2103, 2130, 2301, 2310
				3012, 3021, 3102, 3120, 3201, 3210
			}
			n(E) = 4
			n(S) = n(e)! = 4! = 24
			n(columns) = n(s) / n(e) = 6
			n(rows) = n(s) / n(columns) = 4
			
			Convert index to row and column indexes
			row = floor( index / n(columns) )
			column = index % n(columns)
			Set index by column
			
			Get E[row] as value
			Remove value from E
			Repeat steps until n(E) is equal to zero.
		"""
		
		ne = len( values )
		if ne < 1:
			return ''
		
		ns = MyMathSolver.getFactorialValue( ne )
		if index >= ns:
			raise ValueError( 'Given index exceed maximum index: {0}/{1}'.format( index, ns ) )
		
		ncols = ns / ne
		
		row = index / ncols
		column = index % ncols
		index = column
		
		value = values[ row ]
		values.remove( value )
		return '{0}{1}'.format( value, MyMathSolver.getPermutationString( values, index ) )
	
	
	@staticmethod
	def getFactorialValue( n ):
		""" Compute value of n!.
		"""
	
		return math.factorial( n )
	
	
	@staticmethod
	def getSpellingNumberString( number ):
		""" Spell the number below one thousand.
		"""
	
		numberDict = { 
			1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
			6:'six', 7:'seven', 8:'eight', 9:'nine', \
			11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 
			16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', \
			10:'ten', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 
			60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 
			1000:'thousand' 
		}
		
		numStr = ''
		if number > 999:
			x = number / 1000
			number -= x * 1000
			numStr += numberDict[x] + numberDict[1000]
		
		if number > 99:
			x = number / 100
			number -= x * 100
			numStr += numberDict[x] + numberDict[100]
		
		if number > 0:
			if len(numStr):
				numStr += ' and '
			
			if number in numberDict:
				numStr += numberDict[ number ]
			
			else:
				x = number / 10
				number -= x * 10
				if x in numberDict:
					numStr += numberDict[x*10]
				if len(numStr):
					numStr += '-'
				if number in numberDict:
					numStr += numberDict[ number ]
		
		return numStr
	
	
	@staticmethod
	def getFibonacciNumbersList( fibonacciNumbersList=[1,2], number=100, maxNumber=sys.maxint ):
		""" Generate a list of Fibonacci numbers,
		"""
		
		listLength = len( fibonacciNumbersList )
		if listLength > 1 and listLength < number:
			
			nextFibonacciNumber = fibonacciNumbersList[-1] + fibonacciNumbersList[-2]
			if nextFibonacciNumber > maxNumber:
				return fibonacciNumbersList
			
			else:
				fibonacciNumbersList.append( nextFibonacciNumber )
				MyMathSolver.getFibonacciNumbersList( fibonacciNumbersList, number, maxNumber )
		
		return fibonacciNumbersList
	
	
	@staticmethod
	def getPanDigitalNumbersList( digitNum ):
		""" Generate a list of pan digital numbers.
		"""
	
		panDigitalNumbersList = list()
		if not isinstance( digitNum, int ) or digitNum < 1:
			return panDigitalNumbersList
		
		for num in xrange( 10**( digitNum-1 ), 10**digitNum ):
			numStr = str( num )
			isPanDigitalNum = True
			possibleNumbersList = range( 1, digitNum+1 )
			for char in numStr:
				charNum = int( char )
				if charNum in possibleNumbersList:
					possibleNumbersList.remove( charNum )
				else:
					isPanDigitalNum = False
					break
	
			if isPanDigitalNum:
				panDigitalNumbersList.append( num )
		
		return panDigitalNumbersList
	
	
	@staticmethod
	def getGCD( m, n ):
		""" Compute Great Common Division value of the given m and n.
		"""
		return fractions.gcd( m, n )
	
	
	@staticmethod
	def getLCM( m, n ):
		""" Compute Less Common Multiple value of the given m and n.
		"""
		return ( m * n ) / MyMathSolver.getGCD( m, n )
	
	
	@staticmethod
	def getDivisorTuplesSet( number ):
		""" Get a set of tuples, each tuple contains divisor and quotient. 
		"""
		
		tupleSet = set()
		for divisor in range( 1, int( number**0.5 ) + 1 ):
			( quotient, remainder ) = divmod( number, divisor )
			if remainder == 0:
				tupleSet.add( ( divisor, quotient ) )
		return tupleSet
	
	
	@staticmethod
	def isPrimeNumber( number ):
		""" Is the given number a prime ?
		"""
	
		if not isinstance( number, int ):
			return False
	
		if number < 2:
			return False
	
		if number in ( 2, 3, 5, 7 ):
			return True
	
		if number % 2 == 0:
			return False
	
		for i in xrange( 3, int( number ** 0.5 ) + 1, 2 ):
			if number % i == 0:
				return False
		return True
	
	
	@staticmethod
	def isPalindromicString( string ):
		""" Is the given string a palindromic string?
		"""
		
		#   get length of given string
		stringLength = len( string )
	
		if stringLength == 0:
			return False
		
		elif stringLength == 1:
			return True
	
		elif stringLength == 2:
			return string[0] == string[1]
	
		else:
			#   loop into given string to compare letter
			for i in xrange( 0, int( stringLength / 2 ) ):
				#   if does not match then return False
				if string[ i ] != string[ ( -i - 1 ) ]:
					return False
	
			#   the given string is a palindromic, return true
			return True
