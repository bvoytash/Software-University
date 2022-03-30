word_string = input().split()
palindrome = input()

palindrome_string = [el for el in word_string if el[::-1] == el]

occurrences = [1 for el in palindrome_string if el == palindrome]

print(palindrome_string)
print(f"Found palindrome {len(occurrences)} times")