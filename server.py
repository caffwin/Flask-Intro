"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>Hi! This is the home page. <a href='/hello'>Hello!</a></html>"""

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
         <form action="/diss">
        What's your name? <input type="text" name="person">
        <input type="submit" value="Get insulted!">
        </form>
          <br>

        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <br>
          <br>
          Choose a Compliment:
          <select name="compliment">
            <option value="cool">Cool</option>
            <option value="adorable">Adorable</option>
            <option value="awesome">Awesome</option>
            <option value="smart">Smart</option>  
            <option value="fun">Fun</option>                              
          <br>
       

      </body>
    </html>
    """

@app.route('/diss')
def insulted():
  """Get user by name"""
  player = request.args.get("person")
  insult = choice(["stupid", "weird", "tired", "stinky"])
  return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)


@app.route('/greet')
def greet_person():
    """Get user by name. Use compliment"""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
    

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
