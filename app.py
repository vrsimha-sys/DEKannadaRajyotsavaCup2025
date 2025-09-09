from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/auction')
def auction():
    return render_template('auction.html')

@app.route('/matchday')
def matchday():
    return render_template('matchday.html')

if __name__ == '__main__':
    app.run(debug=True)