# import random
# from models.player import Player
# from models.game_history import GameHistory
# from models.database import Session

# # Define the possible choices for the game
# choices = ['rock', 'paper', 'scissors']

# def determine_winner(player_choice, computer_choice):
#     """Function to determine the winner of the round."""
#     if player_choice == computer_choice:
#         return "tie"
#     elif (player_choice == 'rock' and computer_choice == 'scissors') or \
#          (player_choice == 'paper' and computer_choice == 'rock') or \
#          (player_choice == 'scissors' and computer_choice == 'paper'):
#         return "win"
#     else:
#         return "lose"

# def play_game():
#     """Function to play a round of the game."""
#     # Prompt for player's name and choice interactively
#     player_name = input("Enter your name: ")
#     player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

#     # Check if the player's choice is valid
#     if player_choice not in choices:
#         print("Invalid choice, please select from rock, paper, or scissors.")
#         return

#     session = Session()

#     # Check if the player exists in the database
#     player = session.query(Player).filter(Player.name == player_name).first()
#     if not player:
#         # Create new player if not found
#         player = Player(name=player_name)
#         session.add(player)
#         session.commit()

#     # Computer randomly selects a choice
#     computer_choice = random.choice(choices)

#     # Determine the result of the game
#     result = determine_winner(player_choice, computer_choice)

#     # Store the game history in the database
#     game = GameHistory(
#         player_id=player.id,
#         player_choice=player_choice,
#         computer_choice=computer_choice,
#         result=result
#     )
#     session.add(game)
#     session.commit()

#     print(f"Player chose: {player_choice}")
#     print(f"Computer chose: {computer_choice}")
#     print(f"Result: {result.capitalize()}")

#     # Update player's score based on the result
#     if result == "win":
#         player.score += 1
#     elif result == "lose":
#         player.score -= 1
#     session.commit()

#     session.close()

# def display_game_history(player_name):
#     """Display the game history for a specific player."""
#     session = Session()

#     player = session.query(Player).filter(Player.name == player_name).first()
#     if not player:
#         print(f"No player found with the name {player_name}")
#         return

#     game_history = session.query(GameHistory).filter(GameHistory.player_id == player.id).all()

#     if game_history:
#         print(f"Game History for {player_name}:")
#         for game in game_history:
#             print(f"Game ID: {game.id} | Player: {game.player_choice} | Computer: {game.computer_choice} | Result: {game.result}")
#     else:
#         print(f"No games played yet for {player_name}.")

#     session.close()

# def display_all_players():
#     """Display all players in the database."""
#     session = Session()

#     players = session.query(Player).all()

#     if players:
#         print("Players in the database:")
#         for player in players:
#             print(f"Player ID: {player.id} | Name: {player.name}")
#     else:
#         print("No players found in the database.")

#     session.close()

# def main():
#     """Main function to handle CLI commands."""
    
#     while True:
#         print("\nWelcome to Rock, Paper, Scissors!")
#         print("Please choose an option:")
#         print("1. Play Game")
#         print("2. View Game History")
#         print("3. View All Players")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             play_game()
#         elif choice == '2':
#             player_name = input("Enter player's name to view their game history: ")
#             display_game_history(player_name)
#         elif choice == '3':
#             display_all_pla

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
    player_name = input("Enter your name: ")
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in choices:
        print("Invalid choice, please select from rock, paper, or scissors.")
        return

    session = Session()

    player = session.query(Player).filter(Player.name == player_name).first()
    if not player:
        player = Player(name=player_name)
        session.add(player)
        session.commit()

    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)

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

def delete_player():
    """Function to delete a player and their game history."""
    session = Session()

    player_name = input("Enter the player's name to delete: ")
    player = session.query(Player).filter(Player.name == player_name).first()

    if not player:
        print(f"No player found with the name {player_name}")
        session.close()
        return

    session.query(GameHistory).filter(GameHistory.player_id == player.id).delete()
    session.delete(player)
    session.commit()

    print(f"Player '{player_name}' and their game history have been deleted.")
    session.close()

def update_player():
    """Function to update player's name or score."""
    session = Session()

    player_name = input("Enter the player's name to update: ")
    player = session.query(Player).filter(Player.name == player_name).first()

    if not player:
        print(f"No player found with the name {player_name}")
        session.close()
        return

    print(f"Player '{player_name}' found.")
    update_choice = input("What would you like to update?\n1. Update Name\n2. Update Score\nEnter choice (1 or 2): ")

    if update_choice == '1':
        new_name = input("Enter the new name: ")
        player.name = new_name
        print(f"Player name updated to '{new_name}'.")

    elif update_choice == '2':
        new_score = int(input("Enter the new score: "))
        player.score = new_score
        print(f"Player score updated to {new_score}.")
    else:
        print("Invalid choice. No changes were made.")
        session.close()
        return

    session.commit()
    session.close()

def main():
    """Main function to handle CLI commands."""
    
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Please choose an option:")
        print("1. Play Game")
        print("2. View Game History")
        print("3. View All Players")
        print("4. Delete Player")
        print("5. Update Player")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            player_name = input("Enter player's name to view their game history: ")
            display_game_history(player_name)
        elif choice == '3':
            display_all_players()
        elif choice == '4':
            delete_player()  
        elif choice == '5':
            update_player()  
        elif choice == '6':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
