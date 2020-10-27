def factorielIter(nombre):
	i = 1
	reponse = 1
	while(i<=nombre):
		reponse = reponse*i
		i += 1
	return reponse

print(factorielIter(6))
