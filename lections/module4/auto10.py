from random import randint


def get_random_password():
    rand_pass = ""
    for i in range(8):
        rand_pass += chr(randint(40, 126))
    return rand_pass

print(get_random_password())