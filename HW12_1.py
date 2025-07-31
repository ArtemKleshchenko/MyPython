import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    clean_text = ''
    inside_tag = False
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            clean_text += char

    lines = [line.strip() for line in clean_text.splitlines()]
    non_empty_lines = [line for line in lines if line]

    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write('\n'.join(non_empty_lines))

delete_html_tags('draft.html')
