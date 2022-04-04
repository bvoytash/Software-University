import re

line = input()
mirror_word = []
pattern = r"(@|#)(?P<first_word>[A-Za-z]{3}[A-Za-z]*)\1{2}(?P<second_word>[A-Za-z]{3}[A-Za-z]*)\1"
match_obj = re.finditer(pattern, line)
list_with_dicts = [el.groupdict() for el in match_obj]
if list_with_dicts:
    print(f"{len(list_with_dicts)} word pairs found!")
else:
    print("No word pairs found!")

for dict in list_with_dicts:
    mirror = dict['second_word'][::-1]
    if dict['first_word'] == mirror:
        mirror_word.append(dict)

if mirror_word:
    print("The mirror words are:")
    list = []
    for dict in mirror_word:
        list.append(f"{dict['first_word']} <=> {dict['second_word']}")
    print(", ".join(list))
else:
    print("No mirror words!")
