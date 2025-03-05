"""
Rock, Paper, Scissors - User's choice Vs Computer's Choice
Game rules: 
Rock wins against scissors
Scissors wins against Paper
Paper wins against Rock

Note: Here: 0 = Rock, 1 = Paper and 2 = Scissors

User's choice - 0,1,2 and Computer's choice - 0,1,2

0, 0 - Draw
0, 1 - Comp wins
0, 2 - User wins
1, 0 - User wins
1, 1 - draw
1, 2 - Comp wins
2, 0 - Comp wins
2, 1 - User wins
2, 2 - draw

Pseudocode:
Input User_choice
if 0 > User_choice > 2 then Error
if Comp_choice == User_choice then draw
if Comp_Choice == 2 and User_choice == 0 then User win
if User_choice == 2 and Comp_choice == 0 then Comp win
if Comp_choice > User_choice then User lose
if Comp_choice < User_choice then You Win
exit


"""
import random
user_choice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors, Enter your choice: "))
if user_choice > 3 or user_choice < 0:
    print("Invalid input. Enter valid input between 0 and 2.")
else:
    comp_choice = random.randint(0,2)
    print("Computer chose:", comp_choice)
    if comp_choice == user_choice:
        print("It is a draw")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose")
    elif comp_choice == 2 and user_choice == 0:
        print("You win")
    elif comp_choice > user_choice:
        print("You lose")
    elif comp_choice < user_choice:
        print("You win")


