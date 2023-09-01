message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
offset %= 26
for ch in message:
    if 65<=ord(ch)<=90 or 97<=ord(ch)<=122:
        new_ch = ord(ch) + offset
        if 97<=ord(ch)<=122 and new_ch > 122:
            new_ch -=26
        if 65<=ord(ch)<=90 and new_ch > 90:
            new_ch -=26
    else:
        new_ch = ord(ch)
    encoded_message += (chr(new_ch))    
print (encoded_message)