def decompose(n): 
    res=[]
    i=2 
    while n>1: 
        while n%i==0: 
           res += [i]
           n=n/i 
        i=i+1 
    return res

class Fraction:
	def __init__(self,numerateur, denominateur):
		self.numerateur = numerateur
		self.denominateur = denominateur

	def __mul__(self, other):
		self.numerateur *= other.numerateur
		self.denominateur *= other.denominateur

	def __add__(self, other):
		if(other.denominateur == self.denominateur):
			self.numerateur += other.numerateur
		else:
			"""on rend les deux fractions au meme denominateur pour additioner"""
			a = self.denominateur
			self.numerateur *= other.denominateur

			self.denominateur *= other.denominateur
			other.numerateur *= a
			
			other.denominateur *= a		
			self.numerateur += other.numerateur

	def simplifie(self):
		a = decompose(self.numerateur)	
		b = decompose(self.denominateur)
		if a == b:
			self.numerateur = 1
			self.denominateur = 1
		else:
			for n in a:
				if n in b:
					a.remove(n)
					b.remove(n)
			self.denominateur = 1
			self.numerateur = 1
			for x in a:
				self.numerateur *= x
			for x in b:
				self.denominateur *= x


		print(self.numerateur)
		print (self.denominateur)
