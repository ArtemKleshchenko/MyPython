def format_time(seconds):
    if not (0 <= seconds < 8640000):
        return "Число повинно бути в межах від 0 до 8639999"

    minutes, sec = divmod(seconds, 60)
    hours, min = divmod(minutes, 60)
    days, hrs = divmod(hours, 24)

    hrs = str(hrs).zfill(2)
    min = str(min).zfill(2)
    sec = str(sec).zfill(2)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    return f"{days} {day_word}, {hrs}:{min}:{sec}"

user_input = int(input("Введіть число секунд (0–8639999): "))
print(format_time(user_input))