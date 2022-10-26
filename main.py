import random



player_score = 0

cpu_score = 0

tie_counter = 0

playerDecesion = 'input'

aiDecesion = 'input'


def player_choice():
    global playerDecesion
    playerOptions = ["Rock","Paper","Scissors"]
    playerChoice = input("Please choose between Rock, Paper or Scissors(The choices are case sensitive).\n")
    if playerChoice in playerOptions:
        print("This is a valid choice!")
        playerDecesion = playerChoice
    else:
        print("Not a valid choice choose again")


def cpu_choice():
    global aiDecesion
    aiChoice = ["Rock","Paper","Scissors"]
    aiDecesion = random.choice(aiChoice)



def game_state():
    print("This is the current gamestate of player vs cpu")
    print("Player Score:", player_score)
    print("Cpu Score:", cpu_score)
    print("Tie Counter:", tie_counter)
    player_choice()
    cpu_choice()
    determine_winner()
    game_state()

def determine_winner():
    global player_score
    global cpu_score
    global tie_counter
    global playerDecesion
    global aiDecesion
    print("The player chose:" + playerDecesion)
    print("The ai chose:" + aiDecesion)
    if playerDecesion == "Rock" and aiDecesion == "Scissors":
        print("Player wins the round adding 1 point")
        player_score += 1
    elif playerDecesion == "Scissors" and aiDecesion == "Rock":
        print("Player lost the round adding score to cpue")
        cpu_score += 1
    elif playerDecesion == "Paper" and aiDecesion == "Rock":
        print("Player Won the round adding 1 point")
        player_score += 1
    elif playerDecesion == "Rock" and aiDecesion == "Paper":
        print("Player lost the round adding score to cpu")
        cpu_score += 1
    elif playerDecesion == "Scissors" and aiDecesion == "Paper":
        print("Player Won the round adding 1 point")
        player_score += 1
    elif playerDecesion == "Paper" and aiDecesion == "Scissors":
        print("Player lost the round adding score to cpu")
        cpu_score += 1
    elif playerDecesion == aiDecesion:
        print("Round has tied adding 1 to the tie counter")
        tie_counter += 1
    print("Winner was determined for the round")
def main():
    game_state()


main()

