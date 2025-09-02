# rock-paper-scissors
A simple Python implementation of the classic Rock, Paper, Scissors game where the player competes against the computer. The computer’s choice is generated randomly, and the winner is decided based on the standard rules of the game.

# Rock Paper Scissors Game 🎮

This is a simple **Rock, Paper, Scissors** game written in Python where a player plays against the computer.

## 🚀 Features
- Player chooses between **rock**, **paper**, or **scissors**
- Computer randomly selects one option
- Game decides the winner based on standard rules
- Handles ties and different outcomes

---

## 🛠️ Requirements
- Python 3.x installed on your system

---

## Code
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

## ▶️ How to Run

1. Clone or download this repository  
   ```bash
   git clone https://github.com/<your-username>/rock-paper-scissors.git
   cd rock-paper-scissors
