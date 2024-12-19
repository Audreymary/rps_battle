from models.database import Session, engine, Base
from models.player import Player
from models.game_history import GameHistory

Base.metadata.create_all(bind=engine)

session = Session()
new_player = Player(name="Alice", score=10)
session.add(new_player)
session.commit()

player = session.query(Player).filter(Player.name == "Alice").first()
print(player)

session.close()