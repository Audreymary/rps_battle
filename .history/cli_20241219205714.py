import random
from models.player import Player
from models.game_history import GameHistory
from models.database import Session

# Define the possible choices for the game
choices = ['rock', 'paper', 'scissors']

def determine_winner(player_choice, computer_choice):
    """Function to determine the winner of the round."""
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"

def play_game():
    """Function to play a round of the game."""
    # Prompt for player's name and choice interactively
    player_name = input("Enter your name: ")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Check if the player's choice is valid
    if player_choice not in choices:
        print("Invalid choice, please select from rock, paper, or scissors.")
        return

    session = Session()

    # Check if the player exists in the database
    player = session.query(Player).filter(Player.name == player_name).first()
    if not player:
        # Create new player if not found
        player = Player(name=player_name)
        session.add(player)
        session.commit()

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)

    # Determine the result of the game
    result = determine_winner(player_choice, computer_choice)

    # Store the game history in the database
    game = GameHistory(
        player_id=player.id,
        player_choice=player_choice,
        computer_choice=computer_choice,
        result=result
    )
    session.add(game)
    session.commit()

    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    print(f"Result: {result.capitalize()}")

    # Update player's score based on the result
    if result == "win":
        player.score += 1
    elif result == "lose":
        player.score -= 1
    session.commit()

    session.close()

def display_game_history(player_name):
    """Display the game history for a specific player."""
    session = Session()

    player = session.query(Player).filter(Player.name == player_name).first()
    if not player:
        print(f"No player found with the name {player_name}")
        return

    game_history = session.query(GameHistory).filter(GameHistory.player_id == player.id).all()

    if game_history:
        print(f"Game History for {player_name}:")
        for game in game_history:
            print(f"Game ID: {game.id} | Player: {game.player_choice} | Computer: {game.computer_choice} | Result: {game.result}")
    else:
        print(f"No games played yet for {player_name}.")

    session.close()

def display_all_players():
    """Display all players in the database."""
    session = Session()

    players = session.query(Player).all()

    if players:
        print("Players in the database:")
        for player in players:
            print(f"Player ID: {player.id} | Name: {player.name}")
    else:
        print("No players found in the database.")

    session.close()

def main():
    """Main function to handle CLI commands."""
    
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Please choose an option:")
        print("1. Play Game")
        print("2. View Game History")
        print("3. View All Players")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            player_name = input("Enter player's name to view their game history: ")
            display_game_history(player_name)
        elif choice == '3':
            display_all_players()
        elif choice == '4':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main_":
    main()