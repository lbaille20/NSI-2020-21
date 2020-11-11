def afficher_instructions_utilisateur():
    print('À tout moment, vous pouvez décider de quitter le jeu')
    print('en saisissant le mot "quitter" ou la lettre "q"')

def saisie_nom_joueur(etat_jeu, donnees_joueurs):
    k = etat_jeu['joueur_courant']
    nom = input("Saisir le nom du joueur " + str(k + 1) + " : ")
    return nom

def saisie_coup(etat_jeu, donnees_joueurs):
    joueur_courant = etat_jeu['joueur_courant']
    saisie = input(donnees_joueurs['noms'][joueur_courant]\
                   + ' saisissez votre coup :\n')
    return saisie

def decoder_coup(chaine):
    dictionnaire_lettres = {'A': 0, 'B': 1, 'C': 2}
    lettre, numero = list(chaine)
    ligne, colonne = dictionnaire_lettres[lettre], int(numero) - 1
    return ligne, colonne

def affichage_debut_partie(etat_jeu, donnees_joueurs):
    noms_joueurs = donnees_joueurs['noms']
    joueur_courant = etat_jeu['joueur_courant']
    print(noms_joueurs[joueur_courant], "commence.")

def affiche_etat(etat_jeu, donnees_joueurs):
    plateau = etat_jeu['plateau']
    symboles_joueurs = donnees_joueurs['symboles']
    symboles_plateau = [' '] + symboles_joueurs
    print('-' * (3 + 4))
    for i in range(3):
        for j in range(3):
            print('|' + symboles_plateau[plateau[i][j] + 1], end = '')
        print('|')
    print('-' * (3 + 4))

def affiche_gagnant(donnees_joueurs, resultat):
    joueur_gagnant, trait, numero = resultat
    noms_joueurs = donnees_joueurs['noms']
    if trait == 'ligne':
        identifiant = ['A', 'B', 'C'][numero]
    elif trait == 'colonne':
        identifiant = str(numero + 1)
    else:
        identifiant = ['descendante', 'ascendante'][numero]
    print(noms_joueurs[joueur_gagnant], "gagne sur la", trait, identifiant)

def affichage_fin_jeu(etat_jeu, donnees_joueurs):
    print('fin de jeu')
