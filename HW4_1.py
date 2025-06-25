lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = []

for x in lst:
    if x != 0:
        result.append(x)

zero_count = lst.count(0)
for _ in range(zero_count):
    result.append(0)

print(result)