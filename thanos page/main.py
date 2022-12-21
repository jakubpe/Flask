from flask import Flask, render_template
import data_manipulation
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    quote = get_quote()
    return render_template('thanos_page.html', quote=quote)


def get_quote():
    return random.choice(data_manipulation.quotes_list())


if __name__ == '__main__':
    app.run(debug=True)
