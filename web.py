import os 
import requests
from flask import Flask, render_template, request

REST_URL = os

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html.j2")

@app.route("/about")
def about():
	return render_template("about.html.j2")

@app.route("/article")
def article():
	return render_template("article.html.j2")

@app.route("/data")
def data():
	return render_template("data.html.j2")

@app.route("/test")
def test():
    db.db.collection.insert_one({"": "John"})
    return "Connected to the data base!"

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
