from flask import Flask, render_template, jsonify, request
import os
import json

from services.userService import readUser
from services.movieService import recommendMovies

class CustomFlask(Flask):
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
		variable_start_string="%%",
		variable_end_string="%%",
	))

app = CustomFlask(__name__)

@app.route("/", methods=["GET"])
def index():
	if request.method == "GET":
		return render_template("index.html")

@app.route("/user", methods=["GET"])
def user():
	if request.method == "GET":
		list_user = readUser()
		return jsonify({
			"users" : list_user
		})

@app.route("/movie/<user>", methods=["GET"])
def movie(user):
	if request.method == "GET":
		list_movies = recommendMovies(user)
		return jsonify(list_movies)

if __name__ == "__main__":
	app.run(debug=True)