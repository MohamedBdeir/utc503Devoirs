
import math
def calculerDelta(a,b,c):
	return b*b-4*a*c

def calculerX0(a,b):
	return -b / (2*a)

def calculerX1(b, delta, a):
	return ( -b - math.sqrt(delta)) / (2*a)

def  calculerX2(b, delta, a):
	return (-b + math.sqrt(delta)) / (2*a)

def resoudreSecondDegre():
	a = float(input("Saisir la valeur de a: "))
	b = float(input("Saisir la valeur de b: "))
	c = float(input("Saisir la valeur de c: "))

	delta = calculerDelta(a,b,c)
	

	if(delta < 0):
		return "L'equation n'a pas de solution rellle"
	elif(delta == 0):
		x0 = calculerX0(a,b)
		return x0
	else:
		s1 = calculerX1(b, delta, a)
		s2 = calculerX2(b, delta, a)
		return (s1,s2)
	

