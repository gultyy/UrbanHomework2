def gpa(list_):
    return sum(list_)/len(list_)


gpa_dict = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Sorted names in set "students" by alphabet (convert to list)
students = sorted(students)
stud_num = len(students)  # number of students
i = 0
# Create GPA dictionary
while i < stud_num:
    gpa_dict[students[i]] = gpa(grades[i])
    i += 1

print(gpa_dict)
