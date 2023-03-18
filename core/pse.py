'''
BHO.Add: 20190923 - PrimeSpace Element
'''
import hashlib

class PSE():
	def __init__(self, p, e = 0):
		self.__n = p**e
		self.__p = p
		self.__e = e	
		self.__r = 0
		self.__hash = hashlib.sha256(p.to_bytes(32,byteorder='big')).digest()
	
	def __str__(self):
		return 'PSE[{}][p={}]'.format(self.__hash.hex(), self.__p)
	
	def str(self):
		if self.__r > 1:
			return '{}=[{}^{}].{}'.format(self.__n, self.__p, self.__e, self.__r)
		else:
			return '{}=[{}^{}]'.format(self.__n, self.__p, self.__e)
	
	# Get the current value of p^e
	def val(self):	
		return self.__n
	
	def set(self, N):
		self.__async_set(N)
		print(self.str())
	
	# Set value
	def __async_set(self, N):
		self.__n = N
		self.__factor()
	
	# Get the factor of a number N, return the prime, the exponent & the remain
	def __factor(self):
		e = 0
		r = 0
		p = self.__p
		N = self.__n
		while N != 1:
			r = N % p
			if r != 0:
				break
			else:
				e += 1
				N = int(N/p)
		self.__e = e
		self.__r = N

p1 = PSE(5)
print(p1)
p1.set(225)

p2 = PSE(7)
print(p2)
#p2.set(735)
p2.set(11)
		
if __name__=='__main__':
	print('PSE.MSG: PrimeSpace project, PS Element module. Developed by BHO. Thank you!')


	
	