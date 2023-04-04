from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# csrf = CSRFProtect()
# csrf.init_app(app)


@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True,port=8080)