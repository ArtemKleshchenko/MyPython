while True:
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть оператор (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Помилка: ділення на нуль")
                continue
        else:
            print("Помилка: неправильний оператор")
            continue

        print("Результат:", result)

        again = input("Для того щоб продовжити введіть y: ").lower()
        if again not in ['y']:
            print("Калькулятор завершує свою роботу.")
            break
    except ValueError:
        print("Введіть коректні числа.")