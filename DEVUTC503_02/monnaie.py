class Monnaie:
	def __init__(self, valeur, devise):
		self.valeur = valeur
		self.devise = devise

	def __add__(self, other):
		if self.devise != other.devise:
			raise TypeError("les deux monnais doivent avoir la meme devise")
		else:
			self.valeur += other.valeur

	def __sub__(self, other):
		if self.devise != other.devise:
			raise TypeError("les deux monnais doivent avoir la meme devise")
		else:
			self.valeur -= other.valeur


if __name__ == '__main__':
	m1 = Monnaie(5, 'euros')
	m2 = Monnaie(7, 'euros')
	m1+m2
	assert m1.valeur == 12

	m1 = Monnaie(5, 'euros')
	m2 = Monnaie(7, 'euros')
	m1-m2
	assert m1.valeur == -2
	


	