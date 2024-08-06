#Snake Water Gun
#snake ,water and gun is a variation of the children's game "rock-paper-scissors"
#where players use hand gesture to represent a snake,water,or gun.The gun beats the water.
#write a program to create a snake-water-gun game in python using if-else staTements.
#do not create any fancy GUI.Use proper fuctions to check for win.

import random
list=['Snake','water','gun']
Computer=random.choice(list)
print("Welcome to the Snake,Water,gun game.")
Your_name=input("enter your name: ")
points=[1,2,3,4,5,6,7,8,9,10]
i=0
for i in range(0,10):
    your_chance=input("Enter Snake/water/gun: ")
    print(Computer)
    if your_chance=='Snake' and Computer=='water':
       print(f"{Your_name} you won the game. and your points are {points[i]}")
       #break
       

    elif your_chance=='water' and Computer=='gun':
       print(f"{Your_name} you won the game. and your points are {points[i]}")
       #break

    elif your_chance=='gun' and Computer=='Snake':
       print(f"{Your_name} you won the game. and your points are {points[i]} ")
       #break

    elif your_chance=='water'and Computer=='Snake':
       print(f"{Your_name} you lost the game!! and your points are {points[i]-points[i]}")
       break

    elif your_chance=='Snake'and Computer=='gun':
       print(f"{Your_name} you lost the game!! and your points are {points[i]-points[i]}")
       break

    elif your_chance=='gun'and Computer=='water':
       print(f"{Your_name} you lost the game!! and your points are {points[i]-points[i]}")
       break

    elif your_chance==Computer:
       print(f"Draw!,your points are {points[i]}")
       

    else:
       print("Wrong choice!")
    
    
point=points[i]
    #print(point[i])

print(f"Your total points = {point-1}")





                        
