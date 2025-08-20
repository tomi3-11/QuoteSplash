from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def get_quotes():
    """ This handles the GET requests from the API"""
    quotes = ''
    
    # Fetching data from the API
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    data = response.json()
    
    # Represent the data for use in the templates
    quotes = {
        "random_q": data[0]["q"],
        "author": data[0]["a"]
    }
    
    
    return render_template('quotes.html', quotes=quotes)


# if __name__ == "__main__":
#     app.run(debug=True)
    
    
    