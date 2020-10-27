import os

def factorielRec(nombre):
	if(nombre == 0):
		return 1
	else:
		return nombre * factorielRec(nombre-1)

print(factorielRec(6))
os.system("pause")
