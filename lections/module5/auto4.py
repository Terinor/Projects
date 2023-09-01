def is_check_name(fullname, first_name):

    return (False if fullname.removeprefix(first_name) == fullname else True)


print ( is_check_name("Adam Smasher", "adam"))