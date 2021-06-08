# AS32

import random
checked = []
floors = int(input("How many floors are there?"))
while len(checked) != 10:
    a = random.randint(1, floors)
    if a not in checked:
        checked.append(a)
print(checked)

