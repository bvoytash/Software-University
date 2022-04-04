import re

travel_points = 0
destinations = []
data = input()
pattern = r"(?<=(=|/))(?P<destination>[A-Z][A-Za-z]{2}[A-Za-z]*)(?=\1)"

match_obj = re.finditer(pattern, data)
list_with_dict = [el.groupdict() for el in match_obj]
for dict in list_with_dict:
    points = len(dict["destination"])
    destinations.append(dict["destination"])
    travel_points += points

destinations = ", ".join(destinations)
print(f"Destinations: {destinations}")
print(f"Travel Points: {travel_points}")
