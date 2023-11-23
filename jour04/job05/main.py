L = [1, 2, 3, 4, 5]
print(L)
print(L[1])

def somme():
    global L
    L[3] = L[2] + L[4]
    print(L)

somme()
print(L[4])