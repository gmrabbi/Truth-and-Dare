import random
from cfonts import render
from time import sleep

from cfonts.core import Font

print(render("TRUTH & DARE", align="center", colors=[
      "red", "white"], background="#0ec"))

players = []
items = []


def generator(List_Name, name):
    print("Enter Some " + name)
    while True:
        Name = str(input("> "))
        if Name == "":
            break
        else:
            List_Name.append(Name)


generator(players, "player's name")
generator(items, "item's name in DARE list...")

selected_player, have_to_do = "", ""


def selection(Name1, Name2):
    global selected_player, have_to_do
    if Name1 == players and Name2 == items:
        selected_player = random.choice(players)
    # elif Name2 == items:
        have_to_do = random.choice(items)
    return selected_player, have_to_do


def cmd():
    print("\nDo you want delete " + do + " from the list..?(yes/no)")
    loop = True
    while loop:
        choice = str(input(">")).lower()
        if choice == "yes":
            loop = False
            return True
        elif choice == "no":
            loop = False
            return False
        else:
            print("Sorry wrong input.😣")


layout = True
while layout:
    if len(items) < 1:
        print("\nSorry all are Done..\nNo more item to play right now.")
        layout = False
    else:
        player, do = selection(players, items)
        print("\nPlease Wait .....")
        sleep(1)
        print("it's spnning.....")
        sleep(1.5)
        print("Selected player is : " + player)
        while True:
            choice = str(
                input("\nWhat you want to Choosse .?(Truth/Dare)")).lower()
            if choice == "":
                pass
            elif choice[0] == "t":
                input()
                break
            elif choice[0] == "d":
                sleep(0.5)
                print("Are you Ready..????😛🤩")
                sleep(1)
                print("You have to do : " + do)
                if cmd():
                    items.remove(do)
                break
            else:
                print("Sorry , Wrong input.")
