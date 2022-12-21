from flask import Flask, render_template

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


if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")