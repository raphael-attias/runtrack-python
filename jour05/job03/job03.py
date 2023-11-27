def afficher_triangle(hauteur):
    for i in range(2, hauteur + 1):
        espace = ' ' * (hauteur - i)
        if i == hauteur:
            ligne = espace + '/' + '_' * (2 * i - 3) + '\\'
        else:
            ligne = espace + '/' + ' ' * (2 * i - 3) + '\\'
        print(ligne)


hauteur_triangle = int(input("Entrez la hauteur du triangle : "))
afficher_triangle(hauteur_triangle)
