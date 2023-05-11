import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    First_name = Column(String(250), nullable=False)
    Last_name = Column(String(250), nullable=False)
    Username = Column(String, nullable=False)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)

    def to_dict(self):
        return {}
    
class Liked(Base):
    __tablename__ = 'Liked'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Liked_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    Post_id = Column(Integer, ForeignKey('Post.id'))
    Post = relationship(Post)

    def to_dict(self):
        return {}

class Comments(Base):
    __tablename__ = 'Comments'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Comment = Column(String, nullable=False)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)
    Post_id = Column(Integer, ForeignKey("Post.id"))
    Post = relationship(Post)


    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
