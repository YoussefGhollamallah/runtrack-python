# -*- coding: utf-8 -*-

def nombre(n):
    if n > 0 :
        print(f"{n} est un chiffre positif")
    elif n < 0:
        print(f"{n} est un chiffre négatif")
    else:
        print(f"{n} est un nombre cardinal")

nombre(5)
nombre(-5)
nombre(0)