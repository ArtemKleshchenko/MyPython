import string

def make_hashtag(text):

    translator = str.maketrans('', '', string.punctuation)
    cleaned = text.translate(translator)

    words = cleaned.split()
    capitalized = ''.join(word.capitalize() for word in words)

    hashtag = '#' + capitalized
    return hashtag[:140]

print(make_hashtag("Hillel Is A Good Choice For Studying Python!"))