command = input()

dict_student = {}

while not command == "end":
    course_name = command.split(" : ")[0]
    student_name = command.split(" : ")[1]

    if not course_name in dict_student:
        dict_student[course_name] = [1, student_name]
    else:
        dict_student[course_name][0] += 1
        dict_student[course_name].append(student_name)


    command = input()

dict_student = dict(sorted(dict_student.items(), key=lambda x: -len(x[1])))

for key, value in dict_student.items():
    print(f"{key}: {value[0]}")
    dict_student[key].pop(0)
    sorted_value = list(sorted(dict_student[key]))
    for el in sorted_value:
        print(f"-- {el}")