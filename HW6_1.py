import string

def letters_range(user_input):
    start, end = user_input.split("-")
    letters = string.ascii_letters
    start_index = letters.index(start)
    end_index = letters.index(end)
    return letters[start_index:end_index + 1]

user_input = input("Введіть літери як на прикладі(a-z): ")
result = letters_range(user_input)
print(result)