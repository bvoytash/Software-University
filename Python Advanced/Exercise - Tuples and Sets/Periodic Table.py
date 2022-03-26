def username_line(n):
    usernames = []
    for _ in range (n):
        name = input().split()
        for i in name:
            usernames.append(i)
    return usernames


n = int(input())
users = set(username_line(n))
for user in users:
    print(user)