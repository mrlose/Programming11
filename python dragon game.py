import random
import time
cave=''
dragon=''
def displayIntro():
  print("You are in a land full of dragons and caves\
  some dragons are friendly and some are not. You may need to find weapons.")
  print()
def findWeapon():
  find=''
  while find !='yes' and find !='no':
    print("Will you try to find a weapon first?")
    find=input()
  return find

def receiveWeapon():
  weapon=''
  if find=='yes':
    sword=random.randint(1,2)
    if sword==1:
      print("You found a new sword!")
      weapon=sword
    elif sword==2:
      print("There's no luck in finding a weapon.")
      weapon=''
  if find=='no':
    print("Good luck fighting a dragon bare handed!")
    weapon=''
  return weapon

def chooseCave():

  print("Now you're ready to explore!")
  friendlycave=random.randint(1,2)
  cave=input("There are 2 caves in front of you, you decide to go into cave: ")
  if cave==str(friendlycave):
    print("It is a friendly dragon!")
    dragon='friendly'
  else:
    print("You encountered an evil dragon!")
    dragon='evil'
  return dragon

def meetDragon():
  if dragon=='friendly':
    print("The dragon gives you its treasures!")
  if dragon=='evil':
    print("The evil dragon attacks you!")
    fight=input("Will you fight back?")
    print(fight)
    if fight=='no':
      print("Oh you're gonna give up? Well you're dead!")
    if fight=='yes':
      if weapon=='':
        print("You have no weapon! The dragon eats you!")
      if weapon==1:
        kill=random.randint(1,2)
        if kill==1:
          print("You slayed the dragon and got the treasure!")
        elif kill==2:
          print("You were defeated! The dragon eats you!")

playAgain='yes'
while playAgain=='yes':
    displayIntro()
    find=findWeapon()
    weapon=receiveWeapon()
    dragon=chooseCave()
    meetDragon()
    playAgain = input("Do you want to play again? Yes or no: ")
