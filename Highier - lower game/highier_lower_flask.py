from flask import Flask
import random

app = Flask(__name__)

def generate_number():
    return random.randint(0, 9)


@app.route('/')
def guess_number():
    return '<h1 style="text-align: center">Guess a number!</h1>' \
           '<img style="margin-left:30%" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=40%>'

@app.route('/<int:number>')
def number_page(number):
    if number == generated_number:
        return '<h1 style="text-align: center">Congrats, you guessed right!</h1>' \
               '<img style="margin-left:25%" src="https://media.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif" width=50%>'
    else:
        if number > generated_number:
            return '<h1 style="text-align: center">Too high</h1>' \
                   '<img style="margin-left: 25%" src="https://64.media.tumblr.com/7dc433a7fd2cbc1730886d5ff46af248/tumblr_msm5w1VOR01svk4jmo1_400.gifv" width=50%>'
        else:
            return '<h1 style="text-align: center">Too low</h1>' \
                   '<img style="margin-left: 25%" src="https://media1.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif?cid=ecf05e472lhiw63vc0usmmb5aq6elsivknuoo6u255g8j0r1&rid=giphy.gif&ct=g" width=50%>'


if __name__ == "__main__":
    generated_number = generate_number()
    app.run(debug=True)
