points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    global points
    total_sum = 0
    if len(coordinates) <= 1:
        print(total_sum)
        return total_sum

    
    for i in range(len(coordinates)-1):
        if coordinates[i] <= coordinates[i + 1]:
            point_pair = tuple(sorted((coordinates[i], coordinates[i + 1])))
            total_sum += points[point_pair]
        else:
            point_pair = tuple(sorted((coordinates[i + 1], coordinates[i])))
            total_sum += points[point_pair]
    print(total_sum)       
    return total_sum
        

coord = [0, 1, 3, 2, 0]       
print(calculate_distance(coord))