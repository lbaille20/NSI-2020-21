from interface_utilisateur_morpion_v2 import saisie_coup, decoder_coup

def init_jeu(etat_jeu, donnees_joueurs):
    plateau = [3*[-1] for i in range(3)]
    etat_jeu['plateau'] = plateau

def term_jeu(etat_jeu, donnees_joueurs):
    pass

def coup(etat_jeu, donnees_joueurs):
    plateau = etat_jeu['plateau']
    joueur_courant = etat_jeu['joueur_courant']
    coup_saisi = saisie_coup(etat_jeu, donnees_joueurs)
    if coup_saisi in ('quitter', 'q'):
        etat_jeu['fin'] = True
    else:
        i, j = decoder_coup(coup_saisi)
        jouer_coup(plateau, i, j, joueur_courant)
        etat_jeu['joueur_courant'] = (joueur_courant + 1) % 2

def jouer_coup(plateau, i, j, joueur):
    plateau[i][j] = joueur

def gagnant(etat_jeu):
    plateau = etat_jeu['plateau']
    contenu_lignes_colonnes_diagonales = \
        [[plateau[i][j]   for j in range(3)] for i in range(3)] + \
        [[plateau[i][j]   for i in range(3)] for j in range(3)] + \
        [[plateau[i][i]   for i in range(3)]] + \
        [[plateau[i][2-i] for i in range(3)]]
    ## dictionnaire pour distinguer entre lignes, colonnes et diagonale
    ## si un élément est en position i dans la liste lignes_colonnes_diagonales
    ## la valeur du quotient dans la division euclidienne de i par 3 permet de savoir s'il s'agit
    ## d'une ligne, d'une colonne ou d'une diagonale
    dict_lig_col_diag = {0: 'ligne', 1: 'colonne', 2: 'diagonale'}
    gagnant = None
    for joueur in range(2):
        test_joueur = [joueur] * 3
        if test_joueur in contenu_lignes_colonnes_diagonales:
            indice = contenu_lignes_colonnes_diagonales.index(test_joueur)
            gagnant = (joueur, dict_lig_col_diag[indice // 3], indice % 3)
    return gagnant

