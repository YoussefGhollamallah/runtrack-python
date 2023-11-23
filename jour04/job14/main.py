def my_long_word(longueur_min, phrase):
    mots = []
    mot_actuel = ''
 
    for caractere in phrase:
        if caractere != ' ':
            mot_actuel += caractere
        else:
            if len(mot_actuel) > longueur_min:
                mots.append(mot_actuel)
            mot_actuel = ''

    
    if len(mot_actuel) > longueur_min:
        mots.append(mot_actuel)

    return ' '.join(mots)

resultat = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")

print(resultat)
