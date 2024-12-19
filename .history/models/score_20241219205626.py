from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Score(Base):
    __tablename__ = 'scores'
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    game_id = Column(Integer, ForeignKey('game_history.id'))
    score = Column(Integer, default=0)
    
    player = relationship("Player", back_populates="scores")
    game_history = relationship("GameHistory", back_populates="score")

    def __repr__(self):
        return f"<Score(player_id={self.player_id}, game_id={self.game_id}, score={self.score})>"