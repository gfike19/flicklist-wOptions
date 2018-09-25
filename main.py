from flask import request, redirect, render_template, session, flash, Flask

app = Flask(__name__)
app.config['DEBUG'] = True

movies = []

@app.route("/", methods=['GET'])
def indexGet():
    return render_template("index.html", movies=movies)

@app.route("/add", methods=['POST'])
def addMovie():
    newMovie = request.form['newMovie']
    movies.append(newMovie)
    return render_template("index.html", movies=movies)

@app.route("/remove", methods=['POST'])
def removeMovie():
    oldMovies = request.form.getlist('oldMovies')

    for movie in oldMovies:
        movies.remove(movie)
    return render_template("index.html", movies=movies)

app.run()