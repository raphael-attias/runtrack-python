def distance_walked_per_week(marche, hauteur):
    hauteur_m = hauteur / 100
    total = (marche * hauteur) * 10 * 7 / 100
    print(f"Pour {marche} marches de {hauteur} cm, le gardien parcourt {total} m par semaine.")

    
distance_walked_per_week(200,60)