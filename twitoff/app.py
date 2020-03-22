"""Main application and routing logic for Twitoff."""
# TO RUN THIS:
# FLASK_APP=hello.py flask run (from before when we were running the entire module)
# now we want to point to something inside of the module... the specific package
# FLASK_APP=twitoff:APP flask run
# can also make a shell to play with flask app by doing
# this is like a repl for the app
# FLASK_APP=twitoff:APP flask shell

from flask import Flask
from .models import DB

def create_app():
    """Create and configure an instance of the Flask application."""
    # make the app
    # __name__ returns the name of the module that we are running the code from
    app = Flask(__name__)
    # three slashes make it a relatitive path
    # set it up so that the app knows about the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    # now make it so that the database knows about the app
    DB.init_app(app)


    # set route up and listen to the route
    # here, we are writing a function that will return the information that
    # will be displayed on the website.. the '/' is the homepage.
    @app.route('/')
    @app.route('/home')
    def home():
        # this will be shown when we are on the home page
        return 'Welcome to TwitOff!'
    @app.route('/about')
    def about():
       # this will be shown when we are on the about page
       return 'About this app!'

    # put debug mode on so that we don't have to restart our server each time
    # we want to view a change
    # THIS ISN'T WORKING
    if __name__ == '__main__':
        app.run(debug=True)

    return app