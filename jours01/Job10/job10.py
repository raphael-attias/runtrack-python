montant_initial = int(input("Entrez votre montant initial : "))
taux_rendement_annuel = float(input("Entrez le taux de rendement annuel souhaité (par exemple, 0.2 pour 20%) : "))

montant_apres_un_an = montant_initial * (1 + taux_rendement_annuel)
gain_annuel_initial = montant_apres_un_an - montant_initial

montant_initial += 5000
taux_rendement_annuel += 0.02

montant_apres_un_an = montant_initial * (1 + taux_rendement_annuel)
gain_annuel_apres_augmentation = montant_apres_un_an - montant_initial

montant_initial -= 0.1 * montant_initial
taux_rendement_annuel -= 0.01

montant_apres_un_an = montant_initial * (1 + taux_rendement_annuel)
gain_final = montant_apres_un_an - montant_initial

# ajout de f avant les chaînes pour permettre le formatage
print(f"\nGain annuel initial : {gain_annuel_initial} euros")
print(f"Gain annuel après augmentation de capital : {gain_annuel_apres_augmentation} euros")
print(f"Gain final après retrait : {gain_final} euros")
