wagons = int(input())

wagon_list = [0 for num in range(0, wagons)]
data = input()

while not data == "End":
    command = data.split()
    if "add" in command:
        people = int(command[1])
        wagon_list[-1] += people
    elif "insert" in command:
        index = int(command[1])
        people = int(command[2])
        wagon_list[index] += people
    elif "leave" in command:
        index = int(command[1])
        people = int(command[2])
        wagon_list[index] -= people

    data = input()
print(wagon_list)
