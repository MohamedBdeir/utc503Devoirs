tete = lambda l : l[0]
reste = lambda l: l[1:]


def nombreElements(liste):
    if liste ==[]:
        return 0
    else:
        return 1+nombreElements(reste(liste))

def somme(liste):
    if liste == []:
        return 0
    else:
        return tete(liste)+somme(reste(liste))

def moyenne(liste):
    return somme(liste) / nombreElements(liste)


def inserer(liste, element):
    if nombreElements(liste) == 1:
        if tete(liste) < element:
            return liste + [element]
        else:
            return [element] + liste
    else:
        if tete(liste) < element:
            return [tete(liste)]+inserer(reste(liste), element)
        else:
            return [element]+[tete(liste)]+reste(liste)


def tri(liste):
    if len(liste) <= 1:
        return liste
    else:
        return tri([x for x in reste(liste) if x <= tete(liste)]) + [tete(liste)] +\
            tri([x for x in reste(liste) if x > tete(liste)])



