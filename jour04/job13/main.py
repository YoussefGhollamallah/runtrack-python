L= [10,20,30,20,10,50,60,40,80,50,40]

new_list = []

for i in L:
    if i not in new_list:
        new_list.append(i)

print(new_list)