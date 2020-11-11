def afficher_instructions_utilisateur():
    print('À tout moment, vous pouvez décider de quitter le jeu')
    print('en saisissant le mot "quitter" ou la lettre "q"')
    print('Vous pouvez saisir les lignes en majuscules ou en minuscules.')

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
    dictionnaire_lettres = {'A': 0, 'B': 1, 'C': 2,
                            'a': 0, 'b': 1, 'c': 2}
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
    nlig, ncol = 4, 4
    noms_lignes, nom_colonnes = ['A', 'B', 'C'], [' ', '1', '2', '3']
    print('-' * (2* ncol + 1))
    for j in range(len(nom_colonnes)):
        print('|' + nom_colonnes[j], end = '')
    print('|')
    for i in range(nlig - 1):
        print('|' + noms_lignes[i], end = '')
        for j in range(ncol - 1):
            print('|' + symboles_plateau[plateau[i][j] + 1], end = '')
        print('|')
    print('-' * (2* ncol + 1))

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
