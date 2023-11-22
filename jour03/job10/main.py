def pair_imper(n):
    if (n % 2) == 0:
        if n < 0 :
            print(f"{n} est un chiffre pair et négatif")
        else:
            print(f"{n} est un chiffre pair et positif")
    else :
        if n > 0:
            print(f"{n} est un chiffre impair et positif")
        else:
            print(f"{n} est un chiffre impair et négatif")


pair_imper(2)
pair_imper(7)
pair_imper(-3)