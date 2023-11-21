numbers = range(1,101)
numbers_list = []

for i in numbers:
    numbers_list.append(i)


numbers_list.remove(26)
numbers_list.remove(37)
numbers_list.remove(88)

print(numbers_list)