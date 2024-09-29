# OOP- object oriented programming

# classes- blueprints for copies of a particular thing you're making
# objects- the thing (the child) you make from the class. A copy of the thing you made

import random, os



class FightingMenu:
  # constructor- a function that starts up when you first make a class.
  def __init__(self, PlayerHP, EnemyHP, PlayerMP, EnemyMP):
    self.PlayerHP = PlayerHP
    self.EnemyHP = EnemyHP
    self.PlayerMP = PlayerMP
    self.EnemyMP = EnemyMP
    self.NumEscapes = 0
    self.Fighting = True
    self.PlayerAttacks = {"punch":{"damege":10,"hit%":80},"sword":{"damege":25,"hit%":75
},"bow":{"damege":15,"hit%":70}}

    self.art = '''     
        .-.
       (o.o)
        |m|      /\\
       __|__     ||
     //.=|=.\\\\   ||
    // .=|=. \\\\  ||
    || .=|=.  \\\\ __
    \\\\ .=|=.   \\\\//
     \\\\(_=_)     ||
      (:| |:)    ()
       || ||
       () ()
       || ||
       || ||
     =='   '==

       '''

  def MainUI(self):
    print("-------------------------------------------------")
    print("Health: " + str(self.EnemyHP) + "\n" + "Mana:" + str(self.EnemyMP))
    print(self.art)
    print("-------------------------------------------------")
    print("Health:" + str(self.PlayerHP) + "\n" + "Mana:" + str(self.PlayerMP))
    print("-------------------------------------------------")
    reaction = input(
        "What do you want to do?\n 1. Fight \n 2. Flee \n 3. Items \n").lower(
        )
    if reaction == "fight":
      self.FightUI()
    elif reaction == "flee":
      self.Flee()
    elif reaction == "items":
      self.ItemUI()
    else:
      print("Invalid input")
      os.system("clear")

  def FightUI(self):
    os.system("clear")
    if self.EnemyHP <= 0:
      print("You killed the enemy!")
      self.Fighting = False
    attack = input("What do you want to do?\n 1.Punch\n Test #2 \n Test #3\n").lower()
    hit = random.randint(0,100)
    os.system("clear")
    if "punch" in attack and self.PlayerAttacks["punch"]["hit%"] >= hit:
      self.EnemyHP -= self.PlayerAttacks["punch"]["damege"]
      print("You hit the enemy :) dealt " + str(self.PlayerAttacks["punch"]["damege"])
            + " damege")
      
    elif "sword" in attack and self.PlayerAttacks["sword"]["hit%"] >= hit:
      self.EnemyHP -= self.PlayerAttacks["sword"]["damege"]
      print("You hit the enemy :) dealt " + str(self.PlayerAttacks["sword"]["damege"])
            + " damege")
      
    elif "bow" in attack and self.PlayerAttacks["bow"]["hit%"] >= hit:
        self.EnemyHP -= self.PlayerAttacks["bow"]["damege"]
        print("You hit the enemy :) dealt " + str(self.PlayerAttacks["bow"]["damege"])
            + " damege")
   
    else:
      print("You did not hit the enemy :(")
      
      

  def Flee(self):
    escapes = ((
        (self.PlayerHP * 128 / self.EnemyHP) + 30) * self.NumEscapes) % 256
    number = random.randint(0, 255)
    os.system("clear")
    if number < escapes:
      print("You have fled the battle")
      self.Fighting = False
    else:
      self.NumEscapes += 1
      print("You have not escaped the battle")

  def ItemUI(self):
    pass
