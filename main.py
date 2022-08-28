import random


def get_choice():
  player_choice=input("Type Rock, paper or Scissors: ")
  options=["Rock", "Paper", "Scissors"]
  computer_choice=random.choice(options)
  choices={"Player": player_choice, "Computer":computer_choice}
  return choices

def check_win(player,computer):
  print(f"Player choice is {player},Computer choice {computer}")
  if player==computer:
    return "It's a tie"
  elif player== "Rock":
    if computer== "Paper":
      return "Paper covers Rock, you loose"
    else:
      return "Rock smashes Scissors, you win!"
  
  elif player== "Paper":
    if computer== "Rock":
      return "Paper covers Rock, you win"
    else:
      return "Scissors cuts paper, you loose!"

  elif player== "Scissors":
    if computer== "Rock":
      return "Rock smashes Scissors, you loose"
    else:
      return "Scissors cuts Paper, you win!"

choices=get_choice()
result=check_win(choices["Player"],choices["Computer"])
print(result)




     


