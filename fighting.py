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
    self.Alive = True
    self.PlayerAttacks = {"punch":{"damege":10,"hit%":80},"sword":{"damege":25,"hit%":75
},"bow":{"damege":15,"hit%":70}}
    self.EnemyAttacks = {"punch":{"damege":5,"hit%":50}, "sword":{"damege":15,"hit%":40}}

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
        os.system("cls")

  def FightUI(self):
    os.system("cls")
    misspell = False
      
    attack = input("What do you want to do?\n 1.Punch\n 2. Sword \n 3. Bow \n").lower()
    hit = random.randint(0,100)
    os.system("cls")
    if "punch" in attack and self.PlayerAttacks["punch"]["hit%"] >= hit:
      self.EnemyHP -= self.PlayerAttacks["punch"]["damege"]
      print("You hit the enemy :) dealt " + str(self.PlayerAttacks["punch"]["damege"])
            + " damege")
      misspell = False
      
    elif "sword" in attack and self.PlayerAttacks["sword"]["hit%"] >= hit:
      self.EnemyHP -= self.PlayerAttacks["sword"]["damege"]
      print("You hit the enemy :) dealt " + str(self.PlayerAttacks["sword"]["damege"])
            + " damege")
      misspell = False
      
    elif "bow" in attack and self.PlayerAttacks["bow"]["hit%"] >= hit:
        self.EnemyHP -= self.PlayerAttacks["bow"]["damege"]
        print("You hit the enemy :) dealt " + str(self.PlayerAttacks["bow"]["damege"])
            + " damege")
        misspell = False

    if "punch" not in attack or "sword" not in attack or "bow" not in attack:
      os.system('cls')
      print("Please spell correctly")
      misspell = True
    else:
      print("You did not hit the enemy :(")
    if self.EnemyHP <= 0:
      print("You killed the enemy!")
      self.Fighting = False
      self.Alive = False
    if self.Alive and misspell == False:
      enemy_attack = random.randint(0,100)
      enemy_hit = random.randint(0,100)
      if enemy_attack <= 60:
        if self.EnemyAttacks["sword"]["hit%"]<= enemy_hit:
          self.PlayerHP -= self.EnemyAttacks["sword"]["damege"]
          print("The skeleton swung their sword and dealt 15 damege")
        else:
          print("The skeleton swung thier sword but misses you")
      else:
        if self.EnemyAttacks["punch"]["hit%"] <= enemy_hit:
          self.PlayerHP -= self.EnemyAttacks["punch"]["damege"]
          print("The skeleton punched you and did 5 damege")
        else:
          print("The skeleton tried to punch you but you dodged at the last second")

      
      

  def Flee(self):
    escapes = ((
        (self.PlayerHP * 128 / self.EnemyHP) + 30) * self.NumEscapes) % 256
    number = random.randint(0, 255)
    os.system("cls")
    if number < escapes:
      print("You have fled the battle")
      self.Fighting = False
    else:
      self.NumEscapes += 1
      print("You have not escaped the battle")

  def ItemUI(self):
    pass
