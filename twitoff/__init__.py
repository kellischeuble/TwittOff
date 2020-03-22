"""Entry point for TwitOff Flask application."""
# use '.' because we are in the same directory/package
# if we were outside, we would do twitoff.app
from .app import create_app

APP = create_app()