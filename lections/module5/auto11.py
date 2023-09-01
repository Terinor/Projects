import re

def find_word(text, word):
    result = {
        'result': False,
        'first_index': None,
        'last_index': None,
        'search_string': word,
        'string': text
    }

    match = re.search(r'\b{}\b'.format(re.escape(word)), text, re.IGNORECASE)
    if match:
        result['result'] = True
        result['first_index'] = match.start()
        result['last_index'] = match.end() - 1
        result['search_string'] = match.group()

    return result

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word_to_find = "Python"

result = find_word(text, word_to_find)
print(result)

{'result': True, 'first_index': 34, 'last_index': 40, 'search_string': 'Python', 'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'}
{'result': False, 'first_index': None, 'last_index': None, 'search_string': 'python', 'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'}