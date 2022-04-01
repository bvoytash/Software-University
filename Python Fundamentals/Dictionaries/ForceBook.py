command = input()

corresponding_side = {}

while not command == "Lumpawaroo":

    if len(command.split(" | ")) > 1:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[-1]

        if not force_side in corresponding_side:
            corresponding_side[force_side] = []
            Flag = True
            for key, value in corresponding_side.items():
                if force_user in corresponding_side[key]:
                    Flag = False
                    break
                else:
                    continue
            if Flag:
                corresponding_side[force_side].append(force_user)
        else:
            if force_user not in corresponding_side[force_side]:
                corresponding_side[force_side].append(force_user)

    else:
        command = command.split(" -> ")
        force_side = command[-1]
        force_user = command[0]

        for sides, users in corresponding_side.items():
            if force_user in users:
                corresponding_side[sides].remove(force_user)
        if not force_side in corresponding_side:
            corresponding_side[force_side] = []
            corresponding_side[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!" )
        else:
            corresponding_side[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!" )

    command = input()

corresponding_side = dict(sorted(corresponding_side.items(), key=lambda x: (-len(x[1]), x[0]) ))

for sides, users in corresponding_side.items():
    if users:
        print(f"Side: {sides}, Members: {len(users)}")
        sorted_users = sorted(corresponding_side[sides])
        for names in sorted_users:
            print(f"! {names}")