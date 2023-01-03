from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from settings import DATABASE_URL

database_path = DATABASE_URL
if database_path.startswith('postgres://'):
    database_path = database_path.replace('postgres://', 'postgresql://', 1)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
BaseModel
a entity model base class, extends the base SQLAlchemy Model
'''


class BaseModel(db.Model):
    __abstract__ = True

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


'''
Player
a persistent player entity, extends the base SQLAlchemy Model via BaseModel
'''


class Player(BaseModel):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    goals = Column(Integer)
    assists = Column(Integer)
    country_id = Column(Integer, db.ForeignKey('countries.id'), nullable=False)

    def __init__(self, name, goals, assists, country_id):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.country_id = country_id

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'goals': self.goals,
            'assists': self.assists,
            'country_id': self.country_id
        }


'''
Country
a persistent country entity, extends the base SQLAlchemy Model via BaseModel
'''


class Country(BaseModel):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(Integer)
    coach = Column(String)

    def __init__(self, name, rank, coach):
        self.name = name
        self.rank = rank
        self.coach = coach

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'rank': self.rank,
            'coach': self.coach
        }
