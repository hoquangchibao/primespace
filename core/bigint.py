'''
BHO.Add: 20190923, BigInt class
'''
import sys
import numpy 
import hashlib

class bigint():
	def __init__(self, nbits):
		self.__nbits = nbits
		self.__nbytes = int(nbits/8)
		if(nbits%8) != 0:
			self.__nbytes += 1
			self.nbits = self.__nbytes*8			
		self.__bytes = [self.__nbytes]
		
	def __str__(self):
		return hashlib.sha256(