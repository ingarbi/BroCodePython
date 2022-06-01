##Lesson 37
import random
P_Score = 0
C_Score = 0

while True:
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Lets play, pick - 'rock,paper or scissors': ").lower()
        if player == computer:
            print("Ur choice is "+player)
            print("computer choice is "+computer)
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("Ur choice is " + player)
                print("computer choice is " + computer)
                print("u lost!")
                C_Score +=1
            if computer == "scissors":
                print("Ur choice is " + player)
                print("computer choice is " + computer)
                print("u win!")
                P_Score += 1
        elif player == "paper":
            if computer == "scissors":
                print("Ur choice is " + player)
                print("computer choice is " + computer)
                print("u lost!")
                C_Score += 1
            if computer == "rock":
                print("Ur choice is " + player)
                print("computer choice is " + computer)
                print("u win!")
                P_Score += 1
        elif player == "scissors":
            if computer == "rock":
                print("Ur choice is " + player)
                print("computer choice is " + computer)
                print("u lost!")
                C_Score += 1
            if computer == "paper":
                print("Ur choice is " + player)
                print("computer choice is " + computer)
                print("u win!")
                P_Score += 1

    play_again = input("do yu want to play again(yes/no)").lower()
    if play_again == "yes":
        continue
    elif play_again == "no" or play_again != "yes":
        print("Bye")
        break
print("UR Score " + str(P_Score))
print("PC score " + str(C_Score))
if P_Score > C_Score:
    print("You have won")
elif P_Score < C_Score:
    print("U lost")
else:
    print("TIE!!!")
#########################################################################################################################
import random
p_score = 0
c_score = 0

while True:
    choices = ["r", "p","s"]
    computer = random.choice(choices)
    player_choice = None
    while not player_choice in choices:
        player_choice = input("Please chose r,p or sci:")
        if player_choice == computer:
            print("u chose: ",player_choice,"\nPC chose: " +computer)
            print("It is tie")
        elif player_choice == "r":
            if computer == "s":
                print("You have chosen: " +player_choice)
                print("PC has chosen: "+computer)
                print("YOU WIN")
                p_score +=1
            if computer == "p":
                print("You have chosen: " +player_choice)
                print("PC has chosen: "+computer)
                print("YOU lost")
                c_score += 1
        elif player_choice == "p":
            if computer == "r":
                print("You have chosen: " +player_choice)
                print("PC has chosen: "+computer)
                print("YOU WIN")
                p_score += 1
            if computer == "s":
                print("You have chosen: "+player_choice)
                print("PC has chosen: "+computer)
                print("YOU lost")
                c_score += 1
        elif player_choice == "s":
            if computer == "p":
                print("You have chosen: " +player_choice)
                print("PC has chosen: "+computer)
                print("YOU WIN")
                p_score += 1
            if computer == "r":
                print("You have chosen: " +player_choice)
                print("PC has chosen: "+computer)
                print("YOU lost")
                c_score +=1
    play_again = input("do you want to play again(yes or no):")
    if play_again != "yes":
        break
if p_score == c_score:
    print("U will win next time")
    print("your score: "+str(p_score),"\nComp score :"+str(c_score))
elif p_score > c_score:
    print("Well played")
    print("your score: " + str(p_score), "\nComp score :" + str(c_score))
else:
    print("Next time bro")
    print("your score: " + str(p_score), "\nComp score :" + str(c_score))

######################FRom Tim Tech
import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)
    # rock: 0, paper:1, scissors:2
    if user_input == "rock" and computer_pick == "scissors":
        print("You win")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_wins += 1
    else:
        print("You lost")
        computer_wins += 1
print("You won", + user_wins, "times")
print("Comp wom", computer_wins, "times")
print("Goodbye")


######### Kylie Ying

import random
import math

def play():
    user = input("Choose: 'rock' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False
def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
           print("its tie You and computer have chosen {}. \n".format(user))
        elif result == 1:
            player_wins += 1
            print("You won. You chose {} and computer chose {}.\n".format(user, computer))
        else:
            computer_wins += 1
            print("you chose {} and comp chose {} and you lost.\n".format(user, computer))
        print("\n")
    if player_wins > computer_wins:
        print("You won the best {} games".format(n))
    else:
        print("Sorry computer won best of {} games".format(n))


if __name__ == '__main__':
    play_best_of(3)


