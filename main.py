import os
from fighting import FightingMenu
import enemies
EnemyTypes = [enemies.Skeleton, enemies.Boss_1]
location = {"Cave": ["Dead End", "Fork Path", "Mineshaft", "Campsite", "Exit"],
            "Mountain": ["Cave", "Dragon Nest", "Town", "Trader"],
            "Town": ["Tavern", "Shop", "Blacksmith", "Vendor"],
            "Dungeon": ["Skeleton", "Orc", "Goblin", "Treasure", "Dead End", "Fork Path", "Exit"],
            "Castle": ["Dead End", "Fork Path", "Tavern", "Shop", "Blacksmith", "Vendor",
                       "Quest Board", "Skeleton", "Treasure"],
            "Dragon Nest": ["Treasure Horde", "Dragon", "Princess"]}
locations = list(location.keys())
# gives you back a list of all of the keys within a dictionary

rooms = {
    "Skeleton": enemies.Skeleton,
    "Boss": enemies.Boss_1,
    locations[0]:
        {"description": "You enter a cave.",
         "items": ["broken pickaxe", "unlit torch", "broken sword"],
         "south": location[locations[0]][3],  # mine camp
         "east": "N Hallway 1",
         "north": "Exit"
         },
    location[locations[0]][3]:
        {"description": "You enter an old Campsite.",
         "items": ["rations", "health potion", "shield", "gold pieces", "pickaxe",
                   "flint & steel"],
         "north": locations[0],
         "south": "Skeleton"
         },
    "N Hallway 1":
        {
            "description": "You are now in a hallway.",
            "items": ["helmet"],
            "east": "Hallway",
            "north": locations[0],
            "south": "Mid Hallway 1"
        },
    "Mid Hallway 1":
        {
            "description": "You make your way through the hallway.",
            "items": [],
            "east": "Dead End",
            "west": location[locations[0]][3],
            "north": "N Hallway 1",
            "south": "S Hallway 1"
        },
    "S Hallway 1":
        {
            "description": "You are now in a room.",
            "items": ["gold vase"],
            "east": "S Hallway 2",
            "west": "Treasure room",
            "north": "Mid Hallway 1",
        },
    "S Hallway 2":
        {
            "description": "You are now in a room.",
            "items": [],
            "west": "S Hallway 1",
            "north": "Boss Room"
            # "south": "Exit"

        },
    "Treasure room":
        {
            "description": "You enter a room with a bunch of coins",
            "items": ["gold peices", "gold peices", "gold peices"],
            "east": "S Hallway 1",

        },
    "Boss Room":
        {
            "description": "The door slowly closes behind you",
            "items": ["dead person"],
            "north": "Boss",
            
        },
    "Dead End":
        {
            "description": "You have reached a dead end",
            "items": ["rusty sword"],
            "west": "Mid Hallway 1"

        },
}
player = {
    "current_room": locations[0],
    "inventory": ["sword", "bow"],
    "HP": 100,
    "MP": 100,
    "attacks": [("punch", 15, 85), ("sword", 100, 75), ("bow", 20, 70)]

}


def Inventory():
    answer = "You have these items: "
    answer += ', '.join(player["inventory"])
    print(answer)


def Take(item):
    room_stash = rooms[player["current_room"]]["items"]
    if item in room_stash:
        player["inventory"].append(item)
        room_stash.remove(item)
        print("You have taken the " + item + "\n")
    else:
        print("Please spell correctly")


def ShowDescription(room):
    return rooms[room]["description"]


def navigate(direction):
    current_room = player["current_room"]

    if direction in rooms[current_room]:
        os.system('clear')
        player["current_room"] = rooms[current_room][direction]


    else:
        os.system('clear')
        print("Can't go there!\n")


def status():
    print("You have " + str(player["HP"]) + " health and "+ str(player["MP"])+" magic points")
def Investigate():
    answer = ""
    items_list = rooms[player["current_room"]]["items"]
    if items_list != "":
        for i in items_list:
            select_item = i
            if items_list.index(select_item) == len(items_list) - 1:
                answer += " and"

            if select_item[-1] == "s":
                if items_list.index(select_item) == 0:
                    answer += "There are"
                answer += " some " + select_item.lower() + ','
            else:
                if items_list.index(select_item) == 0:
                    answer += "There is"
                answer += " a " + select_item.lower() + ","
        return answer + "\n"
    else:
        return "There are no items"


FightSkeleton = FightingMenu(player["HP"], rooms["Skeleton"]["HP"], player["MP"], rooms["Skeleton"]["MP"],
                     enemies.Skeleton["attacks"], player["attacks"], enemies.Skeleton["image"], "skeleton")

FightBoss = FightingMenu(player["HP"], rooms["Boss"]["HP"], player["MP"], rooms["Boss"]["MP"],
                     enemies.Boss_1["attacks"], player["attacks"], enemies.Boss_1["image"], "boss")
while True:

    print(ShowDescription(player["current_room"]))
    previous_room = player["current_room"]

    choice = input("What do you want to do? \nMove: N,S,E,W,\nInvestigate\nAttack\netc...\n").lower()
    if "move" in choice:
        if choice[5::] in ["north", "south", "east", "west"]:
            navigate(choice[5::])

        else:
            os.system('clear')
            print("Please print a valid direction, ex: North, South\n")
    elif "investigate" in choice:
        os.system('clear')
        print(Investigate())
    elif "take" in choice:
        os.system('clear')
        Take(str(choice[5::]))
    elif "inventory" in choice:
        os.system('clear')
        Inventory()
    elif "status" in choice:
        status()
    else:
        os.system('clear')
        print("Please use a valid command\n")

    if (player["current_room"] == "Skeleton" and FightSkeleton.Fighting and FightSkeleton.Alive):
        while FightSkeleton.Fighting:
            FightSkeleton.MainUI()

        FightSkeleton.Fighting = True
        player["current_room"] = previous_room

    if (player["current_room"] == "Skeleton" and FightSkeleton.Alive == False):
        rooms["Skeleton"]["description"] = "You enter an empty room with some bones on the ground"
        rooms["Skeleton"]["north"] = location[locations[0]][3]



    if (player["current_room"] == "Boss" and FightBoss.Fighting and FightBoss.Alive):
        while FightBoss.Fighting:
            FightBoss.MainUI()

        FightBoss.Fighting = True
        player["current_room"] = previous_room
        rooms["Boss Room"]["south"] = "S Hallway 2"

    if (player["current_room"] == "Boss" and FightBoss.Alive == False):
        rooms["Boss"]["description"] = "You enter an empty room with a giant pool of sludge on the ground"
        rooms["Boss"]["south"] = "Boss Room"
        
