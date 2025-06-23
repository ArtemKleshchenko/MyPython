lst = [99, 43, 68, 1, 22, 653]

if len(lst) == 0:
    result = [[], []]
else:
    if len(lst) % 2 == 0:
        half = len(lst) // 2
    else:
        half = len(lst) // 2 + 1

    left = []
    right = []

    i = 0
    while i < len(lst):
        if i < half:
            left += [lst[i]]
        else:
            right += [lst[i]]
        i += 1

    result = [left, right]

print(result)
