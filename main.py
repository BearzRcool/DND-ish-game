import os
from fighting import FightingMenu

location = {"Cave": ["Dead End", "Fork Path", "Mineshaft", "Campsite", "Exit"], 
            "Mountain": ["Cave", "Dragon Nest", "Town", "Trader"], 
            "Town" : ["Tavern", "Shop", "Blacksmith","Vendor"] ,
            "Dungeon" : ["Skeleton","Orc","Goblin","Treasure","Dead End","Fork Path","Exit"],
            "Castle" : ["Dead End","Fork Path","Tavern", "Shop", "Blacksmith","Vendor",
                        "Quest Board","Skeleton","Treasure"] ,
            "Dragon Nest" : ["Treasure Horde", "Dragon", "Princess"]}
locations = list(location.keys()) 
# gives you back a list of all of the keys within a dictionary

rooms = {
  "Skeleton":
  {
    "description": "You encounter a skeleton!",
     "inventory":["Spear","Sheild"],
     "HP": 100,
     "MP": 20,
    "Dmg": 10,
    "Crit Dmg": 25,
    "Crit Rate": 10,
    "Head": [60, 8,],
    "Arms": [30, 4,],
    "Torso":[30, 3,],
    "Legs": [20, 2,],
  },
  locations[0]: 
  {"description": "You enter a cave.",
   "items": ["Broken pickaxe", "Unlit torch", "Broken sword"],
   "south": location[locations[0]][3], # mine camp
   "east": "N Hallway 1",
   "north": "Exit" 
  },
  location[locations[0]][3]:
  {"description": "You enter an old Campsite.",
    "items": ["Rations", "Health potion", "Shield","Gold pieces", "Pickaxe",
              "Flint & steel"],
    "east": "Mid Hallway 1",
    "north":locations[0], 
    "south": "Skeleton"
  },
  "N Hallway 1":
  {
    "description": "You are now in a humid hallway.",
    "items": ["Helmet"],
    "east": "Hallway",
    "north":locations[0],
    "south": "Mid Hallway 1"
  },
  "Mid Hallway 1":
  {
    "description": "You are now in a humid hallway",
    "items": [],
    "east": "Dead End",
    "west": location[locations[0]][3],
    "north":"N Hallway 1",
    "south": "S Hallway 1"
  },
  "S Hallway 1":
  {
    "description": "You are now in a humid hallway",
    "items": ["Gold vase"],
    "east": "S Hallway 2",
    "west": "Treasure room",
    "north":"Mid Hallway 1",
  },
  "S Hallway 2":
  {
    "description": "You are now in a humid hallway",
    "items": [],
    "west": "S Hallway 1",
    "north":"Boss Room"
    #"south": "Exit"
  
  },
  "Treasure room":
  {
    "description": "You enter a room with a bunch of coins",
    "items": ["Gold peices", "Gold peices","Gold peices"],
    "west": "S Hallway 1",
  
  },
  "Boss Room":
  {
    "description": "You feel an ominous presence",
    "items": ["Dead person"],
    "north":"Boss",
    "south": "It's closed off"
  },
  "Dead End":
  {
    "description": "You have reached a dead end",
    "items": ["Rusty sword"],
    "west": "Mid Hallway 1"

  },
}
player = {
  "current_room":locations[0],
  "inventory": [],
  "HP" : 100,
  "MP" : 100
}

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

def Investigate():
  answer = ""
  items_list = rooms[player["current_room"]]["items"]
  for i in items_list:
    select_item = i
    if items_list.index(select_item) == len(items_list)-1:
      answer += " and"

    if select_item[-1] == "s":
      if items_list.index(select_item) == 0:
        answer += "There are"
      answer += " some " + select_item.lower() +','
    else:
      if items_list.index(select_item) == 0:
        answer += "There is"
      answer += " a " + select_item.lower() + ","
  return answer


SkeletonFight = FightingMenu(player["HP"],rooms["Skeleton"]["HP"],player["MP"],rooms["Skeleton"]["MP"])


while True:
  print(ShowDescription(player["current_room"]))
  
  
  if(player["current_room"] == "Skeleton"):
    if SkeletonFight.Alive == True:
      while SkeletonFight.Fighting:
        SkeletonFight.MainUI()
      player["current_room"] = previous_room
      if SkeletonFight.Alive == True:
        SkeletonFight.Fighting = True
  previous_room = player["current_room"]
  choice = input("What do you want to do? \nMove: N,S,E,W,\nInvestigate\nAttack\netc...\n").lower()
  if "move" in choice:
    if choice[5::] in ["north","south","east","west"]:
      navigate(choice[5::])
    else:
      os.system('clear')
      print("Please print a valid direction, ex: North, South\n")
  elif "investigate" in choice:
    os.system('clear')
    print(Investigate())
  else:
    os.system('clear')
    print("Please use a valid command\n") 

    
  
  
