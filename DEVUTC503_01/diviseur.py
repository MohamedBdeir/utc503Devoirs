import os

def diviseur(nombre):
	if(nombre == 0):
			return "pas de diviseur"
	elif (nombre ==1):
			return 1
	else:
		i = 2
		while(i<=nombre):
			if( (nombre%i) == 0):
				break
			else:
				i += 1
		if(i == nombre):
			return "pas de diviseur"
		else:
			return i


a = diviseur(49)
print(a)
os.system('pause')