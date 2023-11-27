def diagonal_carpet(n):
    haut= "-" * (n + 1)
    print(f"+{haut}+")
    val = n
    for i in range(n + 1):
        gauche = "#" * val
        droite = "#" * (n - val)
        print(f"|{gauche} {droite}|")
        val -= 1
    print(f"+{haut}+")
diagonal_carpet(10)
