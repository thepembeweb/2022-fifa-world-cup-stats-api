from flask import Flask, request, abort, jsonify
from models import setup_db, Country, Player
from flask_cors import CORS
from auth import AuthError, requires_auth
from utils import paginate_data

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        """ Handle after_request response"""

        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS"
        )

        return response

    @app.route('/')
    def index():
        return 'Welcome to the 2022 FIFA World Cup Stats API!'

# ----------------------------------------------------------------------------#
# Country Controllers.
# ----------------------------------------------------------------------------#

    @app.route('/countries')
    def get_countries():
        """ Get countries """

        try:
            selection = Country.query.all()
            countries = paginate_data(request, selection)
            
            if len(countries) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'countries': countries,
                'total_countries': len(countries)
            })
        except Exception as e:
            print(f'Error occurred in get_countries(): {e}')
            abort(404)

    @app.route('/countries/<int:id>')
    @requires_auth('get:countries-detail')
    def get_country(jwt, id):
        """ Get country by id """

        try:
            country = Country.query.get(id)

            if country is None:
                abort(404)

            return jsonify({
                'success': True,
                'country': country.format()
            })
        except Exception as e:
            print(f'Error occurred in get_country(id): {e}')
            abort(404)

    @app.route('/countries', methods=['POST'])
    @requires_auth('post:countries')
    def create_country(jwt):
        """ Create a country """

        body = request.get_json()

        if not ('name' in body and 'rank' in body and 'coach' in body):
            abort(400)

        name = body.get('name')
        rank = body.get('rank')
        coach = body.get('coach')

        try:
            country = Country(name=name, rank=rank, coach=coach)
            country.insert()

            return jsonify({
                'success': True,
                'country': country.format()
            })

        except Exception as e:
            print(f'Error occurred in create_country(): {e}')
            abort(422)

    @app.route('/countries/<int:id>', methods=['PATCH'])
    @requires_auth('patch:countries')
    def update_country(jwt, id):
        """ Update a country """

        body = request.get_json()

        country = Country.query.get(id)

        if country is None:
            abort(404)

        if body.get('rank'):
            country.title = body.get('rank')
        if body.get('coach'):
            country.coach = body.get('coach')

        try:
            country.update()

            return jsonify({
                'success': True,
                'country': country.format()
            })

        except Exception as e:
            print(f'Error occurred in update_country(id): {e}')
            abort(422)

    @app.route('/countries/<int:id>', methods=['DELETE'])
    @requires_auth('delete:countries')
    def delete_country(jwt, id):
        """ Delete a country """

        country = Country.query.get(id)

        if country is None:
            abort(404)

        try:
            country.delete()

            return jsonify({
                'success': True,
                'deleted': id
            })

        except Exception as e:
            print(f'Error occurred in delete_country(id): {e}')
            abort(422)

# ----------------------------------------------------------------------------#
# Player Controllers.
# ----------------------------------------------------------------------------#

    @app.route('/players')
    def get_players():
        """ Get players """

        try:
            selection = Player.query.all()
            players = paginate_data(request, selection)

            return jsonify({
                'success': True,
                'players': players,
                'total_players': len(players)
            })
        except Exception as e:
            print(f'Error occurred in get_players(): {e}')
            abort(404)

    @app.route('/players/<int:id>')
    @requires_auth('get:players-detail')
    def get_player(jwt, id):
        """ Get player by id """

        try:
            player = Player.query.get(id)

            if player is None:
                abort(404)

            return jsonify({
                'success': True,
                'player': player.format()
            })
        except Exception as e:
            print(f'Error occurred in get_player(id): {e}')
            abort(404)

    @app.route('/players', methods=['POST'])
    @requires_auth('post:players')
    def create_player(jwt):
        """ Create a player """

        body = request.get_json()

        if not (
                'name' in body and 'goals' in body and 'assists' in body and 'country_id' in body):
            abort(400)

        name = body.get('name')
        goals = body.get('goals')
        assists = body.get('assists')
        country_id = body.get('country_id')

        try:
            player = Player(
                name=name,
                goals=goals,
                assists=assists,
                country_id=country_id)
            player.insert()

            return jsonify({
                'success': True,
                'player': player.format()
            })

        except Exception as e:
            print(f'Error occurred in create_player(): {e}')
            abort(422)

    @app.route('/players/<int:id>', methods=['PATCH'])
    @requires_auth('patch:players')
    def update_player(jwt, id):
        """ Update a player """

        body = request.get_json()

        player = Player.query.get(id)

        if player is None:
            abort(404)

        if body.get('goals'):
            player.goals = body.get('goals')
        if body.get('assists'):
            player.assists = body.get('assists')
        if body.get('country_id'):
            player.country_id = body.get('country_id')

        try:
            player.update()

            return jsonify({
                'success': True,
                'player': player.format()
            })

        except Exception as e:
            print(f'Error occurred in update_player(id): {e}')
            abort(422)

    @app.route('/players/<int:id>', methods=['DELETE'])
    @requires_auth('delete:players')
    def delete_player(jwt, id):
        """ Delete a player """

        player = Player.query.get(id)

        if player is None:
            abort(404)

        try:
            player.delete()

            return jsonify({
                'success': True,
                'deleted': id
            })

        except Exception as e:
            print(f'Error occurred in delete_player(id): {e}')
            abort(422)

    @app.errorhandler(400)
    def bad_request(error):
        """ Handle 400 error"""

        return (
            jsonify({
                "success": False,
                "error": 400,
                "message": "bad request"
            }),
            400,
        )

    @app.errorhandler(404)
    def not_found(error):
        """ Handle 404 error"""

        return (
            jsonify({
                "success": False,
                "error": 404,
                "message": "resource not found"
            }),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        """ Handle 422 error"""

        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(AuthError)
    def handle_auth_error(error):
        """ Handle AuthError error"""

        return jsonify({
            "success": False,
            "error": error.status_code,
            'message': error.error
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
