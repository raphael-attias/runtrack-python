def tri(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]


ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri(ma_liste)
print("Liste triée :", ma_liste)

