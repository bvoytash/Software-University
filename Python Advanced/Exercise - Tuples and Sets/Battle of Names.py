n = int(input())
even = []
odd = []
for i in range(1, n + 1):
    name = input()
    current_sum = 0
    for el in name:
        current_sum += ord(el)
    the_result = current_sum // i
    if the_result % 2 == 0:
        even.append(the_result)
    else:
        odd.append(the_result)

a = set(odd)
b = set(even)
if sum(odd) == sum(even):
    result = a.union(b)
    c = [str(el) for el in result]
    print(", ".join(c))
elif sum(odd) > sum(even):
    result = a.difference(b)
    c = [str(el) for el in result]
    print(", ".join(c))
else:
    result = b.symmetric_difference(a)
    c = [str(el) for el in result]
    print(", ".join(c))