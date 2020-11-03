from flask import Flask, request, render_template
import random


app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        'flavor' : request.args.get('flavor'),
        'toppings' : request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"> <br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
        </form>
        """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    user_input_color = request.args.get('color')
    user_input_animal = request.args.get('animal')
    user_input_city = request.args.get('city')
    return f"Wow, I didn't know {user_input_color} {user_input_animal}s lived in {user_input_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results", method="POST">
        Please enter your secret message: <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
        </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    user_input_message = request.form.get('message')
    user_secret_list = sorted(user_input_message)
    #made my own method since I didn't see the starter code at the top, leaving it since i'm proud of my work :D
    def list_to_string(user_list):
        """Converts a list of characters into a string"""
        new_string = ""
        for letter in user_list:
            new_string += letter
        return new_string
    sorted_secret_message = list_to_string(user_secret_list)

    return f"Here's your secret message!<br/>{sorted_secret_message}"
    
    

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    #Below is the remnants of the pre-refactor of the calculator form/results
    # result = ""
    # if operation == 'add':
    #     result = int(operand1 + operand2)
    # elif operation == 'subtract':
    #     result = int(operand1 - operand2)
    # elif operation == 'multiply':
    #     result = int(operand1 * operand2)
    # elif operation == 'divide':
    #     result = float(operand1 / operand2)
    context = {
        'operand1' : int(request.args.get('operand1')),
        'operand2' : int(request.args.get('operand2')),
        'operation' : request.args.get('operation'),
    }
    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        'users_name' : request.args.get('users_name'),
        'wants_compliments' : request.args.get('wants_compliments'),
        'compliment_list' : random.sample(list_of_compliments, k=int(request.args.get('num_compliments')))
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
