lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_lst = []

for x in lst:
    if x != 0:
        new_lst.append(x)

zero_count = lst.count(0)
for _ in range(zero_count):
    new_lst.append(0)
print(new_lst)