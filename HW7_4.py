def common_elements():
    divisible_by3 = {num for num in range(100) if num % 3 == 0}
    divisible_by5 = {num for num in range(100) if num % 5 == 0}
    return divisible_by3 & divisible_by5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')