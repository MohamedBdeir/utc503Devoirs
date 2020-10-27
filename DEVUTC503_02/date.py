class Date:
	__init__(self, jour, mois, annee):
			
		if (jour < 1 or jour > 31) or (mois < 1 or mois> 12) or annee < 0:
			print("cette année ne peut pas être créee")
		else:
			self.jour = jour
			self.mois = mois
			self.annee = annee

