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
    if trait = 'ligne':
        identifiant = ['A', 'B', 'C'][numero]
    elif trait = 'colonne':
        identifiant = str(numero + 1)
    else:
        identifiant = ['ascendante', 'descendante'][numero]
    print(noms_joueurs[joueur_gagnant], "gagne sur la", trait, identifiant)
