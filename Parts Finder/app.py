from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def homepage():

    username = 'ケイジ'
    age = 19
    email = 'keji@example.com'

    return render_template('homepage',
                           username=username,
                           age=age,
                           email=email)

if __name__ == '__main__':
  app.run(host='0.0.0.0')

