# flask_app/models/pokemon.py
from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash
import random

# Pokemon class
class Pokemon:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.rank = data['rank']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Get all Pokemon
    @classmethod
    def get_all(cls):
        query = '''
            SELECT * 
            FROM pokemons 
            ORDER BY `rank`;
        '''
        results = connect_to_mysql().query_db(query)
        if not results:
            return []
        return [cls(row) for row in results]

    # Delete all Pokemon
    @classmethod
    def delete_all(cls):
        query = 'TRUNCATE TABLE pokemons;'
        return connect_to_mysql().query_db(query)

    # Check that each Pokemon is ranked uniquely
    @staticmethod
    def validate_rankings(data):
        is_valid = True
        selected_ranks = []
        for key, value in data.items():
            if value == '0':
                flash(f'Must choose a rank for {key}', 'ranking')
                is_valid = False
            else:
                selected_ranks.append(value)
        if len(selected_ranks) != len(set(selected_ranks)):
            flash('Duplicate ranks are not allowed', 'ranking')
            is_valid = False
        return is_valid

    # Add Pokemon to the database
    @classmethod
    def create_all(cls, data):
        cls.delete_all()
        if not cls.validate_rankings(data):
            return False
        for name, rank in data.items():
            pokemon_data = {'name': name, 'rank': int(rank)}
            query = '''
                INSERT INTO pokemons (name, `rank`, created_at, updated_at) 
                VALUES (%(name)s, %(rank)s, NOW(), NOW());
            '''
            connect_to_mysql().query_db(query, pokemon_data)
        return True

    # Set Pokemon names for the rank forms
    @staticmethod
    def set_names():
        return [
            'Pikachu', 'Charmander', 'Squirtle',
            'Gengar', 'Dragonite', 'JigglyPuff',
            'Snorlax', 'Gyarados', 'Eevee', 'Onix'
        ]

    # Randomize the ranks
    @classmethod
    def randomize(cls, data):
        cls.delete_all()
        numbers = list(range(1, 11))
        random.shuffle(numbers)
        for name, rank in zip(data.keys(), numbers):
            pokemon_data = {'name': name, 'rank': rank}
            query = '''
                INSERT INTO pokemons (name, `rank`, created_at, updated_at)
                VALUES (%(name)s, %(rank)s, NOW(), NOW());
            '''
            connect_to_mysql().query_db(query, pokemon_data)
        return
