from flask_app.config.mysqlconnection import connect_to_mysql
from flask_app import app
from flask import flash
import random

# Pokemon class
class Pokemon:
    DB = 'pokemon_schema'
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
        results = connect_to_mysql(cls.DB).query_db(query)
        if not results:
            return
        pokemons = []
        for row in results:
            pokemon = cls(row)
            pokemons.append(pokemon)
        return pokemons
    
    # Delete all Pokemon
    @classmethod
    def delete_all(cls):
        query = 'TRUNCATE TABLE pokemons;'
        return connect_to_mysql(cls.DB).query_db(query)
    
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
        Pokemon.delete_all()
        if not Pokemon.validate_rankings(data):
            return False
        for key, value in data.items():
            pokemon_data = {'name': key, 'rank': int(value)}
            query = '''
                INSERT INTO pokemons (name, `rank`, created_at, updated_at) 
                VALUES (%(name)s, %(rank)s, NOW(), NOW());
            '''
            connect_to_mysql(cls.DB).query_db(query, pokemon_data)
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
        Pokemon.delete_all()
        numbers = list(range(1, 11))
        random.shuffle(numbers)
        for key, num in zip(data.keys(), numbers):
            pokemon_data = {'name': key, 'rank': num}
            query = '''
                INSERT INTO pokemons (name, `rank`, created_at, updated_at)
                VALUES (%(name)s, %(rank)s, NOW(), NOW());
            '''
            connect_to_mysql(cls.DB).query_db(query, pokemon_data)
        return