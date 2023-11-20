
from decimal import Decimal
# -*- coding: latin-1 -*-

produit = {
    "nom" : "Pomme",
    "prix": 1.15,
    "quantité en stock" : 25
}

affichage_produit = f"les information du produit en vente sont : nom = {produit['nom']}, sont prix est de {produit['prix']} euros/unitaire et la quantiter du stock est de {produit['quantité en stock']}"
print(affichage_produit)

user_acheteur = int(input(f"Combien de {produit['nom']} voulez vous acheter ? "))

quantiter_acheter = int(user_acheteur)
nouvelle_quantiter = int(produit['quantité en stock']-quantiter_acheter )
print(f"vous acheter {quantiter_acheter} {produit['nom']} du coup il reste {nouvelle_quantiter} en stock")
print(f" prix actuel des {produit['nom']} est de {produit['prix']}.")
print(f"Suite à l'inflation de la semaine derniere les prix on augmenter, voici les nouveau prix des {produit['nom']}: ")
inflation = float(produit["prix"] * 0.10)
print(f"Voici les imformations actuelle des {produit['nom']}, prix actuel {produit['prix'] + inflation} et sa quantité en stock est {produit['quantité en stock'] - quantiter_acheter}")