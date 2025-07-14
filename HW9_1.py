def popular_words(text: list[float], words: list[float]) -> float:
    lowered_text = text.lower()
    result = {}
    
    for word in words:
        result[word] = lowered_text.split().count(word)

    return result

assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'

print('OK')