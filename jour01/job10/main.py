solde_depart = 5000
taux_annuel = 2

gain_annuel = solde_depart * taux_annuel / 100 # affiche 100 

# j'enregistre dans une nouvelle variable l'addition du solde de départ avec le taux annuel qui affiche 5100
nouveau_solde = solde_depart + gain_annuel 

print("Premiere annee : ")
print(nouveau_solde) # j'affiche le résultat

# j'enregistre dans une variabe le résultat du retrait de l'investisseur 
taux_retrait = nouveau_solde / 10
print()

# j'enregistre dans la variable le nouveau solde après le retrait
solde_apres_retrait = nouveau_solde - taux_retrait

taux_annuel = 1

gain_annuel = solde_apres_retrait * taux_annuel / 100

nouveau_solde = gain_annuel + solde_apres_retrait
print("Deuxieme annee :")
print(nouveau_solde)