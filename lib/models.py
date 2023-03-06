from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# one-to-many
# a game "has many" reviews
# a review "belongs to" a specific game


# 1. Create Game Model
class Game(Base):

    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    # 4. add the relationship to Game
    reviews = relationship('Review', backref=backref('game'))


    # 5. set __repr__()
    def __repr__(self):
        return f'Game(id={self.id}, ' + \
            f'title={self.title}, ' + \
            f'platform={self.platform})'



# 2.1. cd to lib/, run:  alembic revision --autogenerate -m "Create Game Model"
# 2.2 execute migrations to generate database with Game Model: alembic upgrade head


# 3. Create Review Model and associate it with Game using foreign key
class Review(Base):

    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey('games.id'))

    # set __repr__()
    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'


# 6.1. cd to lib/, run:  alembic revision --autogenerate -m'Add Review Model'
# 6.2. execute migrations to generate database with Review Model: alembic upgrade head
