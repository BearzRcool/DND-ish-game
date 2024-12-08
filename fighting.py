# OOP- object oriented programming

# classes- blueprints for copies of a particular thing you're making
# objects- the thing (the child) you make from the class. A copy of the thing you made

import random, os
import enemies



class FightingMenu:
  # constructor- a function that starts up when you first make a class.
  def __init__(self, PlayerHP, EnemyHP, PlayerMP, EnemyMP, EnemyAttacks, PlayerAttacks, EnemyArt, EnemyName):
    self.PlayerHP = PlayerHP
    self.EnemyHP = EnemyHP
    self.PlayerMP = PlayerMP
    self.EnemyMP = EnemyMP
    self.NumEscapes = 0
    self.Fighting = True
    self.Name = EnemyName

    self.PlayerAttacks = PlayerAttacks
    self.EnemyAttacks = EnemyAttacks

    self.art = EnemyArt
    self.intro = 1
  def MainUI(self):
      if self.intro == 1:
        print("A wild " + self.Name+ " apears!")
        self.intro = 0
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
    misspell = False
      
    attack = input("What do you want to do?\n 1. Punch\n 2. Sword \n 3. Bow \n").lower()
    hit = random.randint(0,100)
    os.system("clear")
    if "punch" == attack and self.PlayerAttacks[0][2] >= hit:
      self.EnemyHP -= self.PlayerAttacks[0][1]
      print("You hit the enemy :) dealt " + str(self.PlayerAttacks[1][1])
            + " damege")
      misspell = False
      
    elif "sword" == attack and self.PlayerAttacks[1][2] >= hit:
      self.EnemyHP -= self.PlayerAttacks[1][1]
      print("You hit the enemy :) dealt " + str(self.PlayerAttacks[1][1])
            + " damege")
      misspell = False
      
    elif "bow" == attack and self.PlayerAttacks[2][2] >= hit:
        self.EnemyHP -= self.PlayerAttacks[2][1]
        print("You hit the enemy :) dealt " + str(self.PlayerAttacks[2][1])
            + " damege")
        misspell = False

    elif "punch" not in attack and "sword" not in attack and "bow" not in attack:
      os.system('clear')
      print("Please spell correctly")
      misspell = True

    else:
      print("You did not hit the enemy :(")

    if self.EnemyHP <= 0:
      print("You killed the enemy!\n")
      self.Fighting = False
    

   
    #EnemyAttacks:
    for attack in range(0,len(self.EnemyAttacks)):  
      if self.Fighting and misspell == False:
        enemy_attack = random.randint(0,100)
        enemy_hit = random.randint(0,100)

        if enemy_attack <= 60:
          if self.EnemyAttacks[attack][2]<= enemy_hit:
            self.PlayerHP -= self.EnemyAttacks[attack][1]
            print("The "+ self.Name + " did "+ str(self.EnemyAttacks[attack][1]) + " to you.")
          else:
            print("The "+ self.Name +" missed you")


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
