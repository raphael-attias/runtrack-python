nom = "chaise"
prix_unitaire = 15
quantite_en_stock = 30
# inflation
inflation = prix_unitaire*1.1
# affichage normalisé
print("\nProduit : ", nom)
print("Au prix de : ", prix_unitaire, "euros")
print("Nombre de produits en stock : ", quantite_en_stock)
# panier
panier = (int(input("quantités souhaité : ")))
# gestion et vérification du stock
stock = panier-quantite_en_stock
if panier > quantite_en_stock:
    print("Le nombre de produit commandé est supérieur au nombre de produits en stock. Veuillez réessayer.")
else:
    print("\ncommande validé")
    cout_global = prix_unitaire*panier
    print("total de la commande : ", cout_global, "euro")
# nouveau affichage du produit
    stock_actuel = quantite_en_stock-panier
    print()
    print("Stock actuel :")
    print("Produit : ", nom)
    print("Au prix de : ", prix_unitaire, "euros")
    print("Nombre de produits en stock : ", stock_actuel)
