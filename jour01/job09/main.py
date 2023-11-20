import codecs
# -*- coding: latin-1 -*-

produit = {
    "nom" : "Pomme",
    "prix": 0.15,
    "quantité en stock" : 25
}

affichage_produit = f"les information du produit en vente sont : nom = {produit['nom']}, sont prix est de {produit['prix']} euros/unitaire et la quantiter du stock est de {produit['quantité en stock']}"
print(affichage_produit)