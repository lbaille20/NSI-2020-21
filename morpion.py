from gestion_morpion import *
from interface_utilisateur_morpion import *

def demarrage(etat_jeu, donnees_joueurs):
    afficher_instructions_utilisateur()
    saisie_nom_joueurs(etat_jeu, donnees_joueurs)
    donnees_joueurs['symboles'] = ['x', 'o']
    choix_premier_joueur(etat_jeu, donnees_joueurs)
    etat_jeu['fin'] = False

def saisie_nom_joueurs(etat_jeu, donnees_joueurs):
    noms_joueurs = ['', '']
    for k in range(2):
        etat_jeu['joueur_courant'] = k
        nom = saisie_nom_joueur(etat_jeu, donnees_joueurs)
        if nom in ('quitter', 'q'):
            etat_jeu['fin'] = True
            return None
        noms_joueurs[k] = nom
    donnees_joueurs['noms'] = noms_joueurs
    
def choix_premier_joueur(etat_jeu, donnees_joueurs):
    from random import randint
    etat_jeu['joueur_courant'] = randint(0, 1)
    
def nouvelle_partie(etat_jeu, donnees_joueurs):
    choix_premier_joueur(etat_jeu, donnees_joueurs)
    affichage_debut_partie(etat_jeu, donnees_joueurs)
    init_jeu(etat_jeu, donnees_joueurs)
    affiche_etat(etat_jeu, donnees_joueurs)
    etat_jeu['fin_de_partie'] = False
    while not (etat_jeu['fin'] or etat_jeu['fin_de_partie']):
        coup(etat_jeu, donnees_joueurs)
        affiche_etat(etat_jeu, donnees_joueurs)
        resultat = gagnant(etat_jeu)
        if resultat:
            affiche_gagnant(donnees_joueurs, resultat)
            etat_jeu['fin_de_partie'] = True

def finir_jeu(etat_jeu, donnees_joueurs):
    term_jeu(etat_jeu, donnees_joueurs)
    affichage_fin_jeu(etat_jeu, donnees_joueurs)
