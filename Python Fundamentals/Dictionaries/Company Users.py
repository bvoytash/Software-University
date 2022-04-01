command = input()
company_dict = {}

while not command == "End":
    company, user = command.split(" -> ")
    if not company in company_dict:
        company_dict[company] = [user]
    else:
        if not user in company_dict[company]:
            company_dict[company].append(user)

    command = input()

company_dict = dict(sorted(company_dict.items(), key= lambda x : x[0]))

for company, user in company_dict.items():
    print(f"{company}")
    for name in user:
        print(f"-- {name}")