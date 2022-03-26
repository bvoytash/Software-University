def recursive_power(number, power, result=1, list=[]):

    if result == number**power:
        return
    result *= number
    list.append(result)
    recursive_power(number, power, result)
    return max(list)


    # for n in range(0, power):
    #     result *= number
    # return result
print(recursive_power(2, 3))