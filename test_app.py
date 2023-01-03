import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Country, Player
from settings import CAPTURER_TOKEN, DATABASE_TEST_URL, REVIEWER_TOKEN, SUPERVISOR_TOKEN

# ----------------------------------------------------------------------------#
# Auth headers.
# ----------------------------------------------------------------------------#
data_reviewer_auth_header = {
    'Authorization': f'Bearer {REVIEWER_TOKEN}'
}

data_capturer_auth_header = {
    'Authorization': f'Bearer {CAPTURER_TOKEN}'
}

data_capture_supervisor_auth_header = {
    'Authorization': f'Bearer {SUPERVISOR_TOKEN}'
}


class FifaWCStatsApiTestCase(unittest.TestCase):
    """This class represents the Fifa WC stats api test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = DATABASE_TEST_URL
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_country = {
            'name': 'England',
            'rank': 5,
            'coach': 'Gary Southgate'
        }

        self.updated_country = {
            'rank': 4,
            'coach': 'Thomas Tuchel'
        }

        self.new_player = {
            'name': 'Richarlison',
            'goals': 3,
            'assists': 0,
            'country_id': 2
        }

        self.updated_player = {
            'name': 'Richarlison',
            'goals': 10,
            'assists': 4,
            'country_id': 2
        }

        self.bad_data = {}

    def tearDown(self):
        """Executed after reach test"""
        pass

# ----------------------------------------------------------------------------#
# Countries Test Suite.
# ----------------------------------------------------------------------------#
    def test_get_countries(self):
        res = self.client().get('/countries', headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['countries']))

    def test_get_country(self):
        res = self.client().get('/countries/1', headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['country']))

    def test_404_get_country(self):
        res = self.client().get('/countries/9999', headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_country(self):
        res = self.client().post(
            '/countries',
            headers=data_capture_supervisor_auth_header,
            json=self.new_country)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['country']))

    def test_400_create_country(self):
        res = self.client().post(
            '/countries',
            headers=data_capture_supervisor_auth_header,
            json=self.bad_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_403_create_country(self):
        res = self.client().post(
            '/countries',
            headers=data_reviewer_auth_header,
            json=self.new_country)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message']['description'],
            'Permission not found.')

    def test_update_country(self):
        res = self.client().patch(
            '/countries/3',
            headers=data_capture_supervisor_auth_header,
            json=self.updated_country)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['country']))

    def test_404_update_country(self):
        res = self.client().patch(
            '/countries/9999',
            headers=data_capture_supervisor_auth_header,
            json=self.updated_country)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_country(self):
        country = Country(
            name='Zimbabwe',
            rank=80,
            coach='John Smith'
        )
        country.insert()

        res = self.client().delete(
            f'/countries/{country.id}',
            headers=data_capture_supervisor_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_403_delete_country(self):
        country = Country(
            name='Japan',
            rank=11,
            coach='Hajime Moriyasu'
        )
        country.insert()

        res = self.client().delete(
            f'/countries/{country.id}',
            headers=data_reviewer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message']['description'],
            'Permission not found.')

    def test_404_delete_country(self):
        res = self.client().delete(
            '/countries/9999',
            headers=data_capture_supervisor_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# ----------------------------------------------------------------------------#
# Players Test Suite.
# ----------------------------------------------------------------------------#
    def test_get_players(self):
        res = self.client().get('/players', headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['players']))

    def test_get_player(self):
        res = self.client().get('/players/1', headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['player']))

    def test_404_get_player(self):
        res = self.client().get('/players/9999', headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_player(self):
        res = self.client().post(
            '/players',
            headers=data_capturer_auth_header,
            json=self.new_player)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['player']))

    def test_400_create_player(self):
        res = self.client().post(
            '/players',
            headers=data_capturer_auth_header,
            json=self.bad_data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_403_create_player(self):
        res = self.client().post(
            '/players',
            headers=data_reviewer_auth_header,
            json=self.new_player)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message']['description'],
            'Permission not found.')

    def test_update_player(self):
        res = self.client().patch(
            '/players/3',
            headers=data_capturer_auth_header,
            json=self.updated_player)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['player']))

    def test_404_update_player(self):
        res = self.client().patch(
            '/players/9999',
            headers=data_capturer_auth_header,
            json=self.updated_player)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_player(self):
        player = Player(
            name='Tom Jones',
            goals=1,
            assists=10,
            country_id=1
        )
        player.insert()

        res = self.client().delete(
            f'/players/{player.id}',
            headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_403_delete_player(self):
        player = Player(
            name='John Smith',
            goals=5,
            assists=7,
            country_id=1
        )
        player.insert()

        res = self.client().delete(
            f'/players/{player.id}',
            headers=data_reviewer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message']['description'],
            'Permission not found.')

    def test_404_delete_player(self):
        res = self.client().delete(
            '/players/9999',
            headers=data_capturer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
