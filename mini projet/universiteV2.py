from Etudiant import *
from Cours import *
from Note import *
from functools import reduce

a = Etudiant("10427", "Bdeir", "Mohamed", "A")
b = Etudiant("10428", "Test", "Test", "B")

c = Cours("utc503", "Paradigmes de programation", "A")
d = Cours("test", "test", "A")

e = Note("10427", "utc503", 5)
f = Note("10428", "utc503", 3)
g = Note("10427", "test", 15)

etudiants = [a, b]
cours = [c,d]
notes = [e,f,g]

def returnNote(n, code):
    if n.codeCours == code:
        return n.note

def moyenneCours(cours):
    listeNotes = list(filter(lambda x: x.codeCours == cours, notes))
    listeValeurs = list(map(lambda x: x.note, listeNotes))
    return  reduce(lambda x,y: x+y, listeValeurs)/len(listeValeurs)

def moyenneEtudiant(etu):
    listeNotes = list(filter(lambda x: x.numEtudiant == etu, notes))
    listeValeurs = list(map(lambda x: x.note, listeNotes))
    return  reduce(lambda x,y: x+y, listeValeurs)/len(listeValeurs)
    
def consulterClasse(idCours):
    listeNotes =  list(filter(lambda x: x.codeCours == idCours, notes))
    return list(map(lambda x: x.note, listeNotes))

def consulterEtudiant(idEtu):
    listeNotes = list(filter(lambda x: x.numEtudiant == idEtu, notes))
    return list(map(lambda x: x.note, listeNotes))

print(consulterEtudiant("10427"))