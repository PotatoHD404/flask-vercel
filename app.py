from flask import Flask, render_template, request, session
from credentials import super_secret


app = Flask(__name__)
# site.com
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
