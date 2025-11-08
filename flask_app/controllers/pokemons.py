from flask_app import app
from flask_app.models.pokemon import Pokemon
from flask import render_template, redirect, request

# Index page
@app.route('/')
def index():
    pokemons = Pokemon.get_all()
    return render_template('index.html', pokemons=pokemons)

# Rank page
@app.route('/rank')
def rank_page():
    pokemons = Pokemon.set_names()
    return render_template('rank.html', pokemons=pokemons)

# Rank process
@app.post('/rank/process')
def rank():
    if not Pokemon.create_all(request.form):
        return redirect('/rank')
    return redirect('/')

# Randomize process
@app.post('/rank/randomize')
def randomize():
    Pokemon.randomize(request.form)
    return redirect('/')