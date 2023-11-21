for i in range(0, 100):
    i += 1
    if (i % 5 == 0 and i % 3 == 0):
        i = "FizzBuzz"
    elif (i % 5 == 0):
        i = "Buzz"
    elif (i % 3 == 0):
        i = "Fizz"
    print(i)