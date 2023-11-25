def my_sort(arr):
    n = len(arr)
    total_coups = 0  # Initialiser le compteur de coups

    for i in range(n):
        # Marquer si un échange a été effectué lors de ce passage
        swapped = False

        # Parcourir la liste jusqu'à l'avant-dernier élément
        for j in range(0, n-i-1):
            # Comparer les éléments adjacents et les échanger si nécessaire
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                total_coups += 1

        # Si aucun échange n'a été effectué, la liste est triée
        if not swapped:
            break

    # Afficher la liste triée et le nombre total de coups
    print("Liste triée :", arr)
    print("Nombre total de coups nécessaires :", total_coups)
    
    return arr

# Exemple d'utilisation
liste_non_triee = [64, 34, 25, 12, 22, 11, 90]
resultat = my_sort(liste_non_triee)
