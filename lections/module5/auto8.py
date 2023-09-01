grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    formatted_list = []
    
    for index, (name, grade) in enumerate(students.items(), start=1):
        formatted_name = name.ljust(10)
        formatted_grade = grade.center(5)
        formated_num = str(grades.get(grade)).center(5)
        formatted_index = str(index).rjust(4)
        
        formatted_row = f"{formatted_index}|{formatted_name}|{formatted_grade}|{formated_num}"
        formatted_list.append(formatted_row)
    
    return formatted_list

def formatted_grades2(students):
    formatted_list = []
    for index, (name, grade) in enumerate(students.items(), start=1):
            formatted_row = "{: >4}|{: <10}|{: ^5}|{: ^5}".format(index, name, grade, grades.get(grade))
            formatted_list.append(formatted_row)
        
    return formatted_list

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades2(students):
    print(el)

print("{:^5}".format("FX"))
print("FX".center(5))


    