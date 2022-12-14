from flask import Flask, render_template, url_for
import datetime
import requests

AGIFY_API = "https://api.agify.io/"
GENDERIZE_API = "https://api.genderize.io/"
app = Flask(__name__)

@app.route('/')
def main_page():
    curr_year = datetime.date.today().year
    return render_template('index_test.html', current_year=curr_year)

@app.route('/guess/<string:name>')
def guess(name):
    """fetches info from genderize and agify apis and displays them on the page
    name = str
    page_output = response from apis
    """

    params = {
        'name': name
    }

    genderize_response = requests.get(url=GENDERIZE_API, params=params)
    agify_response = requests.get(url=AGIFY_API, params=params)

    gender = genderize_response.json()['gender']
    age = agify_response.json()['age']

    return render_template('guess_template.html', name=name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    fake_posts = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(url=fake_posts).json()
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)

