from flask import Flask

# return the name of the module
app = Flask(__name__)

# decorator to route 
@app.route("/")
def hello():
    return "Hello World!"


# TO RUN THEIS:
