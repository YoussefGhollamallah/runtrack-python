def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3


def moyennes():
    note1 = int(input("veuillez entrez une note :"))
    note2 = int(input("veuillez entrez deuxième note :"))
    note3 = int(input("veuillez entrez troisième note :"))

    moyenne_etudiant = note1 + note2 + note3 / 3

    if moyenne_etudiant <= 20 and moyenne_etudiant >= 15:
        print("Très bon élève")
    elif moyenne_etudiant <= 14 and moyenne_etudiant >=11:
        print("Bon élève")
    elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8:
        print("Elève moyen")
    elif moyenne_etudiant <= 7 and moyenne_etudiant >=0:
        print("Elève devant faire des efforts")

print(moyenne(10,10,10))

moyennes()