n1 = float(input("Введіть перше число: "))
operator = input("Введіть оператор (+, -, *, /): ")
n2 = float(input("Введіть друге число: "))

if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Помилка: ділення на нуль"
else:
    result = "Помилка: неправильний оператор"

print("Результат:", result)
