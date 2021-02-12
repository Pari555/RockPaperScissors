# Welcome prompt, include instructions
# Computer is going to randomly choose their weapon, either rock, paper, or scissors.
# 1 = rock
# 2 = paper
# 3 = scissors
# Ask the user to choose their weapon in the form of a number
# Compare the user choice and computer choice and then tell them whether they lost or won.
import random
rockPaperScissors = random.randint(1,3)
print("Welcome to a Game of Rock Paper Scissors")
print("")
print("The instructions to the game is very simple. You just have to choose a number from 1-3 and each number is assigned to a weapon. The computer will also choose a number/weapon randomly and whoever chooses the stronger weapon wins. Just remember the rock beats the scissors and the scissors cuts paper and paper covers a rock.")
print("Rock = 1")
print("Paper = 2")
print("Scissors = 3")
print("")
weapon = int(input("Choose a Number from 1-3: "))
print("")
if(rockPaperScissors == weapon):
  print("There is a tie")
elif(rockPaperScissors == 2 and weapon == 1):
  print("You chose Paper and I chose Rock so you win!")
elif(rockPaperScissors == 1 and weapon == 2):
  print("You chose Rock and I chose Paper so I win!")
elif(rockPaperScissors == 1 and weapon == 3):
  print("You chose Rock and I chose Scissors so you win!")
elif(rockPaperScissors == 3 and weapon == 1):
  print("You chose Scissors and I chose Rock so I win!")
elif(rockPaperScissors == 2 and weapon == 3):
  print("You chose Paper and I chose Scissors so I win!")
elif(rockPaperScissors == 3 and weapon == 2):
  print("You chose Scissors and I chose Paper so you win!")


