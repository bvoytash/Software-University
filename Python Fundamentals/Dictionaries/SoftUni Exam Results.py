users_points_dict = {}
language_count_dict = {}
banned = []
command = input()

while not command == 'exam finished':

    if not "banned" in command:
        username, language, points = command.split("-")
        points = int(points)
        if not username in users_points_dict:
            users_points_dict[username] = [points]
        else:
            users_points_dict[username].append(points)

        if not language in language_count_dict:
            language_count_dict[language] = 0
            language_count_dict[language] += 1
        else:
            language_count_dict[language] += 1

    else:
        banned_user = command.split("-")[0]
        banned.append(banned_user)

    command = input()

max_points_users = {}
for key, value in users_points_dict.items():
    max_points_users[key] = max(value)

max_points_users = dict(sorted(max_points_users.items(), key= lambda x : (-x[1], x[0])))
print("Results:")
for user, points in max_points_users.items():
    if user not in banned:
        print(f"{user} | {points}")

language_count_dict = dict(sorted(language_count_dict.items(), key= lambda x : (-x[1], x[0])))
print("Submissions:")
for l, count in language_count_dict.items():
    print(f"{l} - {count}")