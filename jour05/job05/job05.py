def decalagef(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    message_decode = ""
    for caractere in message:
        if caractere in alphabet:
            position = alphabet.index(caractere)
            nouvelle_position = (position + int(decalage)) % len(alphabet)
            nouveau_caractere = alphabet[nouvelle_position]
            message_decode += nouveau_caractere
        else:
            message_decode += caractere
    return message_decode


message = input("Entrez votre message : ")
decalage = input("Combien de décalage ? ")

resultat = decalagef(message, decalage)
print("Message codé : ", resultat)
