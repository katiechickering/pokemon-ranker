from flask_app import app
from flask_app.controllers import pokemons

if __name__ == '__main__':
    app.run(host='localhost', port=5001)