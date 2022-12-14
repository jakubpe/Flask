from flask import Flask, render_template, url_for
import requests


app = Flask(__name__)

def get_blog_posts():
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return response


@app.route('/')
def home():
    return render_template("index.html", posts=response)

@app.route('/post/<num>')
def get_post(num):
    post = response[int(num)-1]
    return render_template('post.html', num=num, post=post)

if __name__ == "__main__":
    response = get_blog_posts()
    app.run(debug=True)
