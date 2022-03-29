

def password_valid(password):
    is_valid = True
    counter = 0

    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for i in password:
        if i.isdigit():
            counter += 1
        if not i.isalpha() and not i.isdigit():
            is_valid = False
            print("Password must consist only of letters and digits")
            break

    if counter < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid



password = input()

is_valid = password_valid(password)

if is_valid:
    print("Password is valid")