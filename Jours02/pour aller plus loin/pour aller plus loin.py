def est_triangle(a, b, c):
    # Vérifier si la somme de deux côtés est toujours supérieure au troisième côté
    return (a + b > c) and (b + c > a) and (a + c > b)

def type_triangle(a, b, c):
    if a == b == c:
        return "Le triangle est équilatéral."
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Le triangle est isocèle et rectangle."
        else:
            return "Le triangle est isocèle mais non rectangle."
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return "Le triangle est rectangle mais non isocèle."
    else:
        return "Le triangle est quelconque."

# Demander à l'utilisateur les longueurs des côtés du triangle
a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

# Vérifier si les longueurs peuvent former un triangle
if est_triangle(a, b, c):
    # Déterminer le type de triangle
    type_result = type_triangle(a, b, c)
    print(type_result)
else:
    print("Ces longueurs ne peuvent pas former un triangle.")
