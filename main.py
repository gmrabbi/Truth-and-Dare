players = []
items = []


def generator(List_Name, name):
    print("Enter Some " + name + "'s name.")
    while True:
        Name = str(input("> "))
        if Name == "":
            break
        else:
            List_Name.append(Name)


generator(players, "player")
generator(items, "item")

print(players)
print(items)
