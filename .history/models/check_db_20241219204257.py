from sqlalchemy.orm import sessionmaker
from database import engine
from models.player import Player
from models.game_history import GameHistory

Session = sessionmaker(bind=engine)
session = Session()

players = session.query(Player).all()
game_history = session.query(GameHistory).all()

print("Players:", players)
print("Game History:", game_history)

session.close()