list = [
    [99, 43, 68, 1, 22, 653]
]

i = 0
while i < len(list):
    lst = list[i]

    if len(lst) > 1:
        last = lst[-1]
        j = len(lst) - 1
        while j > 0:
            lst[j] = lst[j - 1]
            j -= 1
        lst[0] = last

    print(lst)
    i += 1
