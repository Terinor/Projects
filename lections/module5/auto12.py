import re

def find_all_words(text, word):
    matches = re.findall(r'\b{}\b'.format(re.escape(word)), text, re.IGNORECASE)
    
    return matches

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "Python"

positions = find_all_words(text, word)
print(positions)