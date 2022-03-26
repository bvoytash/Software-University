def username_line(n):
    usernames = []
    for _ in range (n):
        name = input()
        usernames.append(name)
    return usernames


n = int(input())
users = set(username_line(n))
for user in users:
    print(user)