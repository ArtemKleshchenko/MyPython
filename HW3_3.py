def split_list(lst):
    middle = (len(lst) + 1) // 2
    return [lst[:middle], lst[middle:]]

print(split_list([99, 43, 68, 1, 22, 653]))
