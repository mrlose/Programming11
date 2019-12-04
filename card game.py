import random

def playerColor():
    playercardcolor=''
    color=random.randint(1,4)
    if color==1:
        playercardcolor="diamonds"
    if color==2:
        playercardcolor="hearts"
    if color==3:
        playercardcolor="clubs"
    if color==4:
        playercardcolor="spades"
    return playercardcolor

def computerColor():
    computercardcolor=''
    color=random.randint(1,4)
    if color==1:
        computercardcolor="diamonds"
    if color==2:
        computercardcolor="hearts"
    if color==3:
        computercardcolor="clubs"
    if color==4:
        computercardcolor="spades"
    return computercardcolor

def playerNumber():
    playercardnumber=''
    playernumber=random.randint(1,13)
    if playernumber==1:
        playercardnumber='2'
    if playernumber==2:
        playercardnumber='3'
    if playernumber==3:
        playercardnumber='4'
    if playernumber==4:
        playercardnumber='5'
    if playernumber==5:
        playercardnumber='6'
    if playernumber==6:
        playercardnumber='7'
    if playernumber==7:
        playercardnumber='8'
    if playernumber==8:
        playercardnumber='9'
    if playernumber==9:
        playercardnumber='10'
    if playernumber==10:
        playercardnumber='jack'
    if playernumber==11:
        playercardnumber='queen'
    if playernumber==12:
        playercardnumber='king'
    if playernumber==13:
        playercardnumber='ace'
    return playercardnumber,playernumber
    

def computerNumber():
    computercardnumber=''
    computernumber=random.randint(1,13)
    if computernumber==1:
        computercardnumber='2'
    if computernumber==2:
        computercardnumber='3'
    if computernumber==3:
        computercardnumber='4'
    if computernumber==4:
        computercardnumber='5'
    if computernumber==5:
        computercardnumber='6'
    if computernumber==6:
        computercardnumber='7'
    if computernumber==7:
        computercardnumber='8'
    if computernumber==8:
        computercardnumber='9'
    if computernumber==9:
        computercardnumber='10'
    if computernumber==10:
        computercardnumber='jack'
    if computernumber==11:
        computercardnumber='queen'
    if computernumber==12:
        computercardnumber='king'
    if computernumber==13:
        computercardnumber='ace'
    return computercardnumber,computernumber
   

def Compete():
    print("The player's card is---",(playercardnumber),"of",(playercardcolor))
    print("The computer's card is----",(computercardnumber),"of",(computercardcolor))
    if (playernumber)<(computernumber):
          print("You lose! Computer win!")
    if (playernumber)>(computernumber):
          print("You win!")
    if (playernumber)==(computernumber):
          print("You and computer are tied!")

playAgain="yes"
while playAgain=="yes":
    playercardcolor=playerColor()
    computercardcolor=computerColor()
    playercardnumber,playernumber=playerNumber()
    computercardnumber,computernumber=computerNumber()
    Compete()
    playAgain=input("Do you want to play again?")
