from flask_app import app
from flask_app.models import pokemon
from flask import render_template, redirect, request

# Index page
@app.route('/')
def index():
    pokemons = pokemon.Pokemon.get_all()
    return render_template('index.html', pokemons=pokemons)

# Rank page
@app.route('/rank')
def rank_page():
    return render_template('rank.html')

# Rank process
@app.post('/rank_process')
def rank():
    if not pokemon.Pokemon.create_all(request.form):
        return redirect('/rank')
    return redirect('/')

# Randomize process
@app.post('/rank_randomize')
def randomize():
    pokemon.Pokemon.randomize(request.form)
    return redirect('/')