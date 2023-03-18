'''
BHO.Add: 20190923, BigInt class
'''
import sys
import numpy as np
import hashlib

class bigint():
	def __init__(self, nbits):
		self.__nbits = 0
		self.__nbytes = 0
		self.__bytes = None
		self.hash = None
		self.__preset(nbits, True)
		
	def len(self):
		return self.__nbytes
		
	def len_in_bits(self):
		return self.__nbits
	
	def __str__(self):
		return 'BigInt[{}-bit/{}-byte][{}]'.format(self.__nbits, self.__nbytes, self.hash.hex())
	
	def __add__(self, op):
		s1 = self.len_in_bits()
		s2 = op.len_in_bits()
		if(s1 < s2):
			self.__expand(s2)
		
		
		
	def fromInt(self, intVal):
		data = intVal.to_bytes(1,byteorder='big')
		self.fromBytes(data)
		
	def fromHex(self, hexStr):
		try:
			data = bytes.fromhex(hexStr)
			self.fromBytes(data)			
		except Exception as ex:
			print('BHO.EXC: {}', ex)
			raise Exception('BIGINT.EXC: Invalid hex string')
			
	def fromBytes(self, bytesArr):
			self.__bytes = bytesArr
			self.__nbytes = len(self.__bytes)
			self.__nbits = 8*self.__nbytes
			self.__rehash()
			
	def dump(self):
		print(self.__bytes.hex())
	
	def __rehash(self):
		self.hash = hashlib.sha256(self.__bytes).digest()
	
	def __expand(self, nbits):
		self.__preset(nbits, False)
		
	def __preset(self, nbits, reset):
		self.__nbits = nbits
		self.__nbytes = int(nbits/8)
		if(nbits%8) != 0:
			self.__nbytes += 1
			self.__nbits = self.__nbytes*8
		if reset:
			self.__bytes = np.zeros(self.__nbytes,dtype=np.uint8).tobytes('C')
		else:
			self.__bytes.resize(self.__nbytes)			
		self.hash = hashlib.sha256(self.__bytes).digest()		
'''
Self Test
'''
bInt = bigint(16)
bInt.fromInt(1)
bInt.dump()
exit()
		
if __name__=='__main__':
	print('BIGINT.MSG: PrimeSpace project, BigInt module. Developed by BHO. Thank you!')