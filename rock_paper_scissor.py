import random
def get_choices():
    player_choices = input("enter the player choices(rock,paper,scissor : )")
    options = ["rock","paper","scissor"]
    computer_choices = random.choice(options)
    choices = {"player":player_choices,"computer":computer_choices}
    return choices


def check_win(player,computer):
    print(f"You choose {player}, computer choose {computer}")

    if player == computer:
        return "it's a tie"
    elif player == "rock":
      if computer == "scissor":
          return "rock smashes scissor! You Win"
      else: 
          return "Paper covers rock! You Lose"
    elif player == "paper":
      if computer == "rock":
          return "Paper covers rock! You Win"
      else: 
          return "Scissors cuts the paper! You lose"
    elif player == "scissor":
      if computer == "paper":
          return "Scissors cuts the paper! You Win"
      else: 
          return "Rock smashes the scissors! You lose"  


choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)