class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        new_person = Person(self.name, other.surname)
        return new_person

class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = [obj for obj in people]

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        both_group = []
        for obj in self.people:
            both_group.append(obj)
        for obj in other.people:
            both_group.append(obj)
        new_group = Group(f"{self.name} {other.name}", both_group)
        return new_group

    def __repr__(self):
        result = [repr(obj) for obj in self.people]
        return f"Group {self.name} with members {', '.join(result)}"

    def __getitem__(self, key):
        return f'Person {key}: {str(self.people[key])}'


# p1 = Person("boro", "voytash")
# p2 = Person("pesho", "peshev")
# # print((p1 + p2).__dict__)
# # print(repr(p1))
# g1 = Group("Grupata")
# g1.people.append(p1)
# g1.people.append(p2)
# print(len(g1))
# g2 = Group("Vtora")
# g2.people.append(p1 + p2)
# print((g1 + g2).people)
# print(repr(g1))
p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)


