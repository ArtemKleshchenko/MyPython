import keyword
import string

user_input = input("Введіть ім'я змінної: ")

def is_valid_variable_name(name: str) -> bool:
    if name in keyword.kwlist:
        return False
    if name.count('_') > 1:
        return False
    if name[0].isdigit():
        return False
    for char in name:
        if char.isupper():
            return False
        if char in string.punctuation and char != "_":
            return False
        if char.isspace():
            return False
    return True

print(f"Результат: {is_valid_variable_name(user_input)}")