"""SQLAlchemy models for TwitOff."""

from flask_sqlalchemy import SQLAlchemy

# make database
DB = SQLAlchemy()

# specify connection string
# we are using sqlite for now
# a model is a class
# the model (here it is User, is a subclass of the Model parent class)
class User(DB.Model):
    """Twitter users that we pull and analyze Tweets for."""
    # define fields
    # use types.. we will want to use generic types 
    # make id field that is a column 
    # will probably want to change Integer to BigInteger later
    id = DB.Column(DB.Integer, primary_key=True)
    # make up to 15 because that is the max len for a Twitter handle
    # nullable=False because it is required.
    handle = DB.Column(DB.String(15), nullable=False)

    # define representation method to give us the string that we 
    # will get when looking in the terminal
    def __repr__(self):
        return f'<User {self.handle}>'


# make Tweet model
class Tweet(DB.Model):
    """Tweets."""
    id = DB.Column(DB.Integer, primary_key=True)
    # max length for a tweet is 280
    text = DB.Column(DB.Unicode(280))
    # going to add a reference from tweet to user ID so we
    # can make a relational database with a one to many relationship
    # (one person, many tweets)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    # make a user field. this won't change the database, but it will allow us to return
    # user object when using the command line
    # allows us to get from tweets to user, and from user to tweets... generated at execution
    # time (not in the database because that would be inneficient)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    # define representation
    def __repr__(self): 
       return f'<Tweet {self.text}' 