def compteur(p):
    longueur = 0
    for lettre in p:
        longueur += 1
    return longueur


def my_long_word(n, phrase):
    mots_apres_n = ""
    verifier_mot = ""

    for lettre in phrase:
        if lettre != " ":
            verifier_mot += lettre
        else:
            if compteur(verifier_mot) > n:
                mots_apres_n += verifier_mot + " "
            verifier_mot = ""
    if compteur(verifier_mot) > n:
        mots_apres_n += verifier_mot

    return mots_apres_n


resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print(resultat)
