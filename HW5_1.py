import keyword
import string

name = input("Введіть ім'я змінної: ")

valid = True

if name in keyword.kwlist:
    valid = False
elif name and name[0].isdigit():
    valid = False
elif name:
    underscore_count = 0
    for char in name:
        if char.isupper():
            valid = False
            break
        if char in string.punctuation and char == "_":
            valid = False
            break
        if char.isspace():
            valid = False
            break
        if char == "_":
            underscore_count += 1

    if underscore_count == len(name):
        valid = False

print(f"Результат: {valid}")