L = [25, 1, 50, 7, 32, 11]



def triage(l):
    n = len(l)
    for i in range(n):
         for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

triage(L)

liste_ordonnee = L

print(liste_ordonnee)