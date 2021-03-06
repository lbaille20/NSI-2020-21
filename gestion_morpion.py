from interface_utilisateur_morpion import saisie_coup, decoder_coup

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
    ## examen des lignes
    for i in range(3):
        ligne = [plateau[i][j] for j in range(3)]
        if ligne == [0, 0, 0]:
            return (0, 'ligne', i)
        elif ligne == [1, 1, 1]:
            return (1, 'ligne', i)
    ## examen des colonnes
    for j in range(3):
        colonne = [plateau[i][j] for i in range(3)]
        if colonne == [0, 0, 0]:
            return (0, 'colonne', j)
        elif ligne == [2, 2, 2]:
            return (1, 'colonne', j)
    ## examen de la diagonale descendante, numérotée 0
    diagonale = [plateau[i][i] for i in range(3)]
    if diagonale == [0, 0, 0]:
        return (0, 'diagonale', 0)
    elif diagonale == [2, 2, 2]:
        return (1, 'diagonale', 0)
    ## examen de la diagonale ascendante, numérotée 1
    diagonale = [plateau[i][2-i] for i in range(3)]
    if diagonale == [0, 0, 0]:
        return (0, 'diagonale', 1)
    elif diagonale == [1, 1, 1]:
        return (1, 'diagonale', 1)
    ## si aucun joueur n'a gagné
    return None
