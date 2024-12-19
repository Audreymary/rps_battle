import random
from models.player import Player
from models.game_history import GameHistory
from database import Session

choices = ['rock', 'paper', 'scissors']

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'paper' and computer_choice == 'rock') or \
       (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_round(player_name, player_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)

    # Initialize session to interact with database
    session = Session()

    # Check if player exists or create new player
    player = session.query(Player).filter_by(name=player_name).first()
    if not player:
        player = Player(name=player_name)
        session.add(player)
        session.commit()

    # Record game history in the database
    game_history = GameHistory(player_choice=player_choice, computer_choice=computer_choice, result=result, player=player)
    session.add(game_history)

    # Update score based on game result
    if result == "You win!":
        player.score += 1
    elif result == "Computer wins!":
        player.score -= 1
    session.commit()

    session.close()
    return result, computer_choice