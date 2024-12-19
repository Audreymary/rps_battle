from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class GameHistory(Base):
    __tablename_= 'game_history'

    id = Column(Integer, primary_key=True)
    player_choice = Column(String, nullable=False)
    computer_choice = Column(String, nullable=False)
    result = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey('players.id'))  # ForeignKey to players table
    
    # Relationship back to Player (You can access the player object from GameHistory)
    player = relationship("Player", back_populates="games")

    def _repr_(self):
        return f"<GameHistory(player_choice={self.player_choice}, computer_choice={self.computer_choice}, result={self.result})>"