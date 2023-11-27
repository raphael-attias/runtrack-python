def afficher_tapis_diagonale(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                if i == 0 or i == n:
                    print(" ", end=" ")
                else:
                    print("#", end=" ")
            else:
                print(" ", end=" ")
        print()

taille_tapis = int(input("Entrez la taille du tapis : "))
print("+" + "-" * ((taille_tapis + 1) * 2 - 3) + "+")
afficher_tapis_diagonale(taille_tapis)
print("+" + "-" * ((taille_tapis + 1) * 2 - 3) + "+")
