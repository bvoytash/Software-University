happiness = [int(el) for el in (input().split())]
factor = int(input())

happiness_factor = [nums * factor for nums in happiness]

average = sum(happiness_factor) / len(happiness_factor)

happiness_employees = [employees for employees in happiness_factor if employees >= average]

if len(happiness_employees) < (len(happiness) / 2):
    print(f"Score: {len(happiness_employees)}/{len(happiness)}. Employees are not happy!")
else:
    print(f"Score: {len(happiness_employees)}/{len(happiness)}. Employees are happy!")


