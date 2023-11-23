L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]


new_L = []


for i in L:
    if i % 2 == 0:
        new_L.append(i)

sum_multiple = sum(new_L)
print(sum_multiple)