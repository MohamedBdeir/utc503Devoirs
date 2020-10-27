from Etudiant import *
from Cours import *
from Note import *
from functools import reduce
class BD:
    def __init__(self, etudiants, cours, notes):
        self._etudiants = etudiants
        self._cours = cours
        self._notes = notes

    def _getEtudiants(self):
        return self._etudiants
    def _setEtudiants(self, etudiants):
        self._etudiants = etudiants
    etudiants = property(_getEtudiants, _setEtudiants)

    def _getCours(self):
        return self._cours
    def _setCours(self, cours):
        self._cours = cours
    cours = property(_getCours, _setCours)

    def _getNotes(self):
        return self._notes
    def _setNotes(self, notes):
        self._notes = notes
    notes =property(_getNotes, _setNotes)

    def ajouterEtudiant(self, numero, nom, prenom, niveau):
        """methode qui créee un étudiant et l'ajoute dans la liste"""
        a = Etudiant(numero, nom, prenom, niveau)
        self._etudiants.append(a)
        print("L'etudiant a bien ete ajoute")
        
    def supprimerEtudiant(self, id):
        """methode qui supprime l'etudiant avec le numero renseigné"""
        for e in self._etudiants:
            if e.numero == id:
                self._etudiants.remove(e)
                print("L'etudiant a bien ete supprime")
    
    def editerEtudiant(self, id, nom, prenom, niveau):
        succes = False
        for e in self._etudiants:
            if id == e.numero:
                e.nom = nom
                e.prenom = prenom
                e.niveau = niveau
                succes = True
        if not succes:
            print("Echec de la modification")
        else:
            print("Etudian modifie avec succes")

    def ajouterCours(self, code, nom, niveau):
        c = Cours(code, nom, niveau)
        self._cours.append(c)
        print("Cours ajoute avec succees")

    def supprimerCours(self, id):
        """methode qui supprime un cours avec le numero renseigné"""
        succes = False
        for e in self._cours:
            if e.code == id:
                self._cours.remove(e)
                succes = True
        if succes:
            print("Le cours a ete supprime")
        else:
            print("Echec de la suppression du cours")

    def editeCours(self, coursId, intitutle, niveau):
        """methode qui modifie l'intitule et le niveau du cours indentifie par coursId"""
        for e in self._cours:
            if e.code == coursId:
              e.intitule = intitutle
              e.niveau = niveau

    def ajouterNote(self, idEtudiant, idCours, note):
        etudiantsId = []
        for e in self._etudiants:
            etudiantsId.append(e.numero)
        coursId = []
        for c in self._cours:
            coursId.append(c.code)
        
        if idEtudiant in etudiantsId and idCours in coursId:
            n = Note(idEtudiant, idCours, note)
            self._notes.append(n)
            print("la note a bien ete ajoutee")
        else:
            print("Le cours ou l'etudiant n'existe pas")

    def supprimerNote(self, idEtudiant, idCours):
        succes = False
        for n in self._notes:
            if n.numEtudiant == idEtudiant and n.codeCours == idCours:
                self._notes.remove(n)
                print("La note a bien ete supprimee")
        
        if not succes:
            print("Echec de la modification de la note")
        else:
            print("La note a bien ete modifiee")

    def editerNote(self, idEtudiant, idCours, valeur):
        for n in self._notes:
            if note.numEtudiant == idEtudiant and note.codeCours == idCours:
                n.note = valeur

    def moyenneClasse(self, idCours):
        notes = []
        for n in self._notes:
            if n.codeCours == idCours:
                notes.append(n.note)
        return sum(notes) / len(notes)

    def moyenneEtudiant(self, idEtudiant):
        notes = []
        for n in self._notes:
            if n.numEtudiant == idEtudiant:
                notes.append(n.note)
        return sum(notes) / len(notes)
    
    def consulterNotesClasse(self, cours):
        res = {}
        for n in self._notes:
            res[n.numEtudiant] = n.note
        return res
    
    def consulterNotesEtudiant(self, etu):
        res = {}
        for n in self._notes:
            if n.numEtudiant == etu:
                res[n.codeCours] = n.note
        return res
    
    """METHODES AVEC MAP FILTER ET REDUCE"""
    def moyenneClassV2(self, idCours):
        notes = []
        notes = list(filter(lambda x.note: x.codeCours == idCours, self._notes))
        return (reduce(lambda x,y : x+y, notes)/len(notes))
