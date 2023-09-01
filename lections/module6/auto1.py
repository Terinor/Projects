import re

def total_salary(path):
    salary_list = []
    total_salary = 0
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        #print(line)
        salary_list.append([float(s) for s in re.findall(r'\b\d+\b', line)])
        #print(salary_list)
        if not line:
            break
        
    for salaries in salary_list:
        for salary in salaries:
            total_salary += salary

    fh.close()

    return total_salary

salFile = ('D:\Projects\lections\module6\salaries.txt')

print(total_salary(salFile))