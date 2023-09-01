def is_spam_words(text, spam_words, space_around=False):
    text.lower()
    split_text = text.split()
    if space_around:
        for word in split_text:
            for spam_word in spam_words:
                if  word.endswith(spam_word + '.'):
                    return True
    else:
        for spam_word in spam_words:
            if spam_word in text:
                return True
    return False



print(is_spam_words('Молох бог ужасен.', ['лох'], space_around= True))