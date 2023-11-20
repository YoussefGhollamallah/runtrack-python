import codecs
# -*- coding: latin-1 -*-

produit = {
    "nom" : "Pomme",
    "prix": 0.15,
    "quantité en stock" : 25
}

affichage_produit = f"les information du produit en vente sont : nom = {produit['nom']}, sont prix est de {produit['prix']} euros/unitaire et la quantiter du stock est de {produit['quantité en stock']}"
print(affichage_produit)

user_acheteur = int(input(f"Combien de {produit['nom']} voulez vous acheter ? "))

quantiter_acheter = int(user_acheteur)

print(f" vous acheter {quantiter_acheter} {produit['nom']} du coup il reste {int(produit['quantité en stock']) - quantiter_acheter} {produit['nom']} en stock")