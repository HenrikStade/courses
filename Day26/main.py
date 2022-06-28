number = [1, 2, 3]
new_list = []

for n in number:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)


# new_list = [new_item for item in list]

new_list = [x+1 for x in number]
print(new_list)

name = "Henrik"
new_list = [letter for letter in name]
print(new_list)

# new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
new_list = [name for name in names if len(name) < 5]
print(new_list)

import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)


student_dict = {"student": ["Angela", "James", "Lily"],
                "score": [56, 76, 98]}
for (key, value) in student_dict.items():
    print(value)


import pandas as pd


student_df = pd.DataFrame(student_dict)
print(student_df)

# for (key, value) in student_df.items():
#     print(value)

for (index, row) in student_df.iterrows():
    print(row.score)