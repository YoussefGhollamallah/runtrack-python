liste_nombre = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Fonction pour arrondir un nombre à l'entier le plus proche
def arrondir(nombre):
    partie_entiere = int(nombre)
    partie_decimale = nombre - partie_entiere
    if partie_decimale >= 0.5:
        return partie_entiere + 1
    else:
        return partie_entiere


n = len(liste_nombre)
for i in range(n):
    for j in range(0, n-i-1):
        # Comparaison et échange
        if arrondir(liste_nombre[j]) > arrondir(liste_nombre[j+1]):
            liste_nombre[j], liste_nombre[j+1] = liste_nombre[j+1], liste_nombre[j]

# Afficher la liste arrondie et triée
print("Liste arrondie et triée :", liste_nombre)
