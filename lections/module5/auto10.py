def formatted_numbers():
    formatted_table = ["| decimal  |   hex    |  binary  |"]
    for i in range(16):
        formatted_table.append("|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i))
    return formatted_table

for el in formatted_numbers():
    print(el)