from BD import *
bd = BD([], [], [])

bd.ajouterEtudiant("10427", "Bdeir", "Mohamed", "A")
bd.ajouterEtudiant("10428", "TEST", "TEST", "B")

bd.ajouterCours("utc503", "Paradigmes de programation", "A")
bd.ajouterCours("test", "test", "A")

bd.ajouterNote("10427", "utc503", 11)
bd.ajouterNote("10428", "utc503", 12)
bd.ajouterNote("10427", "test", 15)

print(bd.consulterNotesEtudiant("10427"))

bd.moyenneClassV2("utc503")