from sqlalchemy import Column, Integer, String
from models.database import Base
from sqlalchemy.orm import relationship

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    score = Column(Integer, default=0)

    # Relationship to GameHistory (a player can have multiple game histories)
    games = relationship("GameHistory", back_populates="player")

    def _repr_(self):
        return f"<Player(name={self.name}, score={self.score})>"