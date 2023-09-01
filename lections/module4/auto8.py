def game(terra, power):
    for sector in terra:
        for loot in sector:
            if power >= loot:
                power += loot
            else:
                break
    print (power)        
    return power

terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power = 1

print(game(terra, power))