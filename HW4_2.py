lst = [2, 10, 6]

if len(lst) == 0:
    print(0)
else:
    suma = 0
    index = 0

    for x in lst:
        if index % 2 == 0:
            suma += x
        index += 1

    result = suma * lst[-1]
    print(result)