lst = [2, 9.3, [947, 2], [999, 0]]
mid = len(lst) // 2
lst = [lst[:mid], lst[mid:]]
print(lst)