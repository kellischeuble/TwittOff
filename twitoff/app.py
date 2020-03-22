"""Main application and routing logic for Twitoff."""
# TO RUN THIS:
# FLASK_APP=hello.py flask run (from before when we were running the entire module)
# now we want to point to something inside of the module... the specific package
# FLASK_APP=twitoff:APP flask run
# can also make a shell to play with flask app by doing
# this is like a repl for the app
# FLASK_APP=twitoff:APP flask shell

from flask import Flask

def create_app():
    """Create and configure an instance of the Flask application."""
    # make the app
    # __name__ returns the name of the module that we are running the code from
    app = Flask(__name__)

    # set route up and listen to the route
    @app.route('/')
    def root():
        return 'Welcome to TwitOff!'
    return app