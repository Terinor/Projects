def split_list(grade):
    if not grade:
        return [], []

    average_score = sum(grade) / len(grade)
    below_average = [score for score in grade if score <= average_score]
    above_average = [score for score in grade if score > average_score]

    return below_average, above_average

# Приклад використання
student_scores = [75, 88, 60, 92, 78, 45, 85, 70]
below_average_scores, above_average_scores = split_list(student_scores)

print("Below average scores:", below_average_scores)
print("Above average scores:", above_average_scores)