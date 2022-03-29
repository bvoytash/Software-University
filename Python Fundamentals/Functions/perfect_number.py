

def perfect(num):
    is_perfect = False
    sum_devisors = 0
    for nums in range(1, num):
        if num % nums == 0:
            sum_devisors += nums
        if sum_devisors == num:
            is_perfect = True
            break


    return is_perfect

number = int(input())
is_perfect = perfect(number)

if is_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

