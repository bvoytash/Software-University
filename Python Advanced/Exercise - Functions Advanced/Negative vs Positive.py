def find_numbers(numbers):
    positive = [el for el in numbers if el > 0]
    negative = [el for el in numbers if el < 0]
    return sum(positive), sum(negative)

numbers = [int(el) for el in input().split()]

positive = find_numbers(numbers)[0]
negative = find_numbers(numbers)[1]

if positive > abs(negative):
    print(negative)
    print(positive)
    print("The positives are stronger than the negatives")
else:
    print(negative)
    print(positive)
    print("The negatives are stronger than the positives")