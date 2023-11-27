message = input("entrez votre message : ")
decalage = input("combien de decallage ? ")


def decalagef(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for caractere in message:
        position = alphabet.index(caractere)
        nouvelle_position = (position + decalage) % len(alphabet)
        nouveau_caractere = alphabet[nouvelle_position]
        decalage += nouveau_caractere
    return decalage


decalagef(decalage)
