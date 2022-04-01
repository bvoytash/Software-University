n = int(input())

student_dict = {}

for _ in range(0, n):
    name = input()
    grade = float(input())

    if name not in student_dict:
        student_dict[name] = [grade]
    else:
        student_dict[name].append(grade)

average_student_grade = {}

for key, value in student_dict.items():
    final_result = sum(value) / len(value)
    if final_result >= 4.50:
        average_student_grade[key] = final_result

average_student_grade = dict(sorted(average_student_grade.items(), key= lambda x : -x[1]))

for key, value in average_student_grade.items():
    print(f"{key} -> {value:.2f}")

