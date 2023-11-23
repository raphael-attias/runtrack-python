def my_long_word(taille_minimale, phrase):
    mots_plus_longs = ""
    mot_actuel = ""
    espace = ' '

    for caractere in phrase:
        # Si le caractère n'est pas un espace, ajoute-le au mot actuel
        if caractere != espace:
            mot_actuel += caractere
        else:
            # Si le mot actuel a une longueur supérieure à la taille minimale, ajoute-le à la chaîne résultante
            if mot_actuel and len(mot_actuel) > taille_minimale:
                if mots_plus_longs:
                    mots_plus_longs += ' '
                mots_plus_longs += mot_actuel

            mot_actuel = ""

    # Vérifie le dernier mot après la boucle
    if mot_actuel and len(mot_actuel) > taille_minimale:
        if mots_plus_longs:
            mots_plus_longs += ' '
        mots_plus_longs += mot_actuel

    return mots_plus_longs
