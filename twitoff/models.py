"""SQLAlchemy models for TwitOff."""

from flask.sqlalchemy import SQLAlchemy

# make database
DB = SQLAlchemy()

# specify connection string
# we are using sqlite for now
# a model is a class
# the model (here it is User, is a subclass of the Model parent class)
class User(Db.Model):
    """Twitter users that we pull and analyze Tweets for."""
    # define fields
    # use types.. we will want to use generic types 
    # make id field that is a column 
    # will probably want to change Integer to BigInteger later
    id = DB.Column(DB.Integer, primary_key=True)
    # make up to 15 because that is the max len for a Twitter handle
    # nullable=False because it is required.
    handle = DB.Column(DB.String(15), nullable=False)

# make Tweet model
class Tweet(DB.Model):
    """Tweets."""
    id = DB.Column(DB.Integer, primary_key=True)
    # max length for a tweet is 280
    test = DB.Column(DB.Unicode(280))