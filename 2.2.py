number = int(input("Введіть п'ятицифрове число: "))

first_digit = number // 10000
second_digit = (number // 1000) % 10
third_digit = (number // 100) % 10
fourth_digit = (number // 10) % 10
fifth_digit = number % 10

reversed_number = fifth_digit * 10000 + fourth_digit * 1000 + third_digit * 100 + second_digit * 10 + first_digit

print(reversed_number)
