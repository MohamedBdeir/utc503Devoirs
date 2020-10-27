import os
def calculer(a,x,n):
	resultat = 0
	i = 0
	while(i<=n):
		resultat = resultat + (a*i*x*i)
		i +=1
	return resultat

b = calculer(2,3,5)
print(b)
os.system("pause")


