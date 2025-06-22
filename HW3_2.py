def last_to_first(lst):
    if len(lst) > 1:
        return [lst[-1]] + lst[:-1]
    return lst

print(last_to_first([5, 9, 3, 12, 49, 13, 23, 65, 81]))