from morpion_v2 import *

etat_jeu, donnees_joueurs = {}, {}
demarrage(etat_jeu, donnees_joueurs)
while not etat_jeu['fin']:
    nouvelle_partie(etat_jeu, donnees_joueurs)
finir_jeu(etat_jeu, donnees_joueurs)
