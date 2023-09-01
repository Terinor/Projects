import re

def replace_spam_words(text, spam_words):
    def replace_with_stars(match):
        return '*' * len(match.group(0))
    
    pattern = r'\b(?:' + '|'.join(map(re.escape, spam_words)) + r')\b'
    result = re.sub(pattern, replace_with_stars, text, flags=re.IGNORECASE)
    return result