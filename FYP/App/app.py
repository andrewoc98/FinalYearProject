from flask import Flask, render_template, url_for
import pandas as pd
def getGraph():

   return Price

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/DJIA')
def DJIA():
        return render_template('Djia.html')

if __name__ == '__main__':
    app.run(debug=True)