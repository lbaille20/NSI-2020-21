from gestion_morpion import *
from affichages_morpion import *

def afficher_instructions_utilisateur():
    print('À tout moment, vous pouvez décider de quitter le jeu en saisissant le mot "quitter" ou la lettre "q"')

def saisie_nom_joueurs(etat_jeu, donnees_joueurs):
    noms_joueurs = ['', '']
    for k in range(2):
        saisie_nom = input("Saisir le nom du joueur " + str(k + 1) + " : ")
        if saisie_nom in ('quitter', 'q'):
            etat_jeu['fin'] = True
            return None
        noms_joueurs[k] = saisie_nom
    donnees_joueurs['noms'] = noms_joueurs
    
def choix_premier_joueur(etat_jeu):
    from random import randint
    etat_jeu['joueur_courant'] = randint(0, 1)

def demarrage(etat_jeu, donnees_joueurs):
    afficher_instructions_utilisateur()
    saisie_nom_joueurs(etat_jeu, donnees_joueurs)
    donnees_joueurs['symboles'] = ['x', 'o']
    choix_premier_joueur(etat_jeu)
    etat_jeu['fin'] = False
    
def nouvelle_partie(etat_jeu, donnees_joueurs):
    noms_joueurs = donnees_joueurs['noms']
    joueur_courant = etat_jeu['joueur_courant']
    print(noms_joueurs[joueur_courant], "commence")
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
