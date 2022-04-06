data = input().split('\\')
the_file = data[-1]

the_name = the_file.split(".")
print(f"File name: {the_name[0]}")
print(f"File extension: {the_name[1]}")