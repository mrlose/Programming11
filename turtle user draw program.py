import turtle
counter=0
distance = 10
angle = 10
while counter<1:
      distance=int(input("Please enter a distance: "))
      angle=int(input("Please enter an angle: "))
      turtle.forward(distance)
      turtle.setheading(angle)
      if distance==0:
            counter=counter+1

print('What an amazing drawing!!!!')
