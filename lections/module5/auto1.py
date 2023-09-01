string1 = 'Alex\nKdfe23\t\f\v.\r'
string2 = 'Al\nKdfe23\t\v.\r'

def real_len(text):
    i = 0
    control_chars = ["\n", "\f", "\r", "\t", "\v"]
    for char in text:
        if char not in control_chars:
            i += 1
    return i
    #return [char for char in text if char not in control_chars]

print (real_len(string1))
print (real_len(string2))

print (string1)
print (string2)