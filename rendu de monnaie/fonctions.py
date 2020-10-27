billets = (1000,5000)
aRendre = {}
aRendre [5000] = 0
aRendre [1000] = 0
def rendreMonnaieFonctionnelle(somme, systeme, aRendre):

    systeme = sorted(systeme)
    if somme - systeme[-1]<0:
        return rendreMonnaieFonctionnelle(somme, systeme[:len(systeme)-1], aRendre)
    if somme - systeme[-1] >0:
        aRendre[systeme[-1]] +=1
        somme -= systeme[-1]
        return rendreMonnaieFonctionnelle(somme, systeme, aRendre)
    if somme-systeme[-1] == 0:
        aRendre[systeme[-1]] +=1
        somme -= systeme[-1]
        return aRendre


def rendreMonnaieImperative(somme, systeme, aRendre):

    systeme = tuple(reversed(systeme))
    for x in systeme:
        nombreDeBillets = somme // x
        somme = somme - nombreDeBillets * x
        aRendre[x] = nombreDeBillets

    return aRendre 


