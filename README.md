# 2022 FIFA World Cup Stats Api

> The 2022 FIFA World Cup Stats Api demonstrates role-based access for data capture supervisors, reviewers, capturers as well as the general public to administer and view player statistics from the 2022 FIFA World Cup hosted in Qatar.

![](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

## 2022 FIFA World Cup Stats Api URL

Visit the website [https://world-cup-2022-stats-api.herokuapp.com](https://world-cup-2022-stats-api.herokuapp.com/)

## Overview

The application showcases the following features:

- Display player statistics.
- Add, edit and delete player statistics.
- Display countries participating in the world cup.
- Add, edit and delete countries.
- Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
- DRY (don't repeat yourself) principles of class and method design.
- Working with modules and packages in Python.
- Coding best practices for style and documentation
- Ensuring that code, docstrings, and comments adhere to [PEP 8 Standards](https://www.python.org/dev/peps/pep-0008/).

## Installation

### Requirements

The project requires `pip` installed.

If you do not have `pip` installed, you can download it here: [pip](https://pip.pypa.io/en/stable/installing/)

### Setup

1. \*\*Create an empty database (fifa-wc) in postgres locally:

```sh
$ createdb -U postgres fifa-wc
```

2. \*\*Create an empty test database (fifa-wc_test) in postgres locally:

```sh
$ createdb -U postgres fifa-wc_test
```

3. \*\*Clone the source locally:

```sh
$ git clone https://github.com/thepembeweb/2022-fifa-world-cup-stats-api.git
```

4. \*\*Navigate to the application folder:

```sh
$ cd 2022-fifa-world-cup-stats-api
```

5. **Initialize and activate a virtualenv using:**

```
python -m virtualenv env
source env/bin/activate
```

> **Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:

```
source env/Scripts/activate
```

6. \*\*Install project dependencies:

```sh
$ pip install -r requirements.txt
```

7. **Run the development server:**

```
export FLASK_APP=app.py
export FLASK_ENV=development # enables debug mode
flask run
```

8. **Verify on the Browser**<br>
   Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000)

9. \*\*Testing:

To deploy the tests, run

```bash
dropdb fifa-wc_test
createdb fifa-wc_test
psql fifa-wc_test < fifa-wc_test.psql
python test_app.py
```

## API Reference

### Getting Started

- Base URL: This app is hosted at the following base URL, `https://world-cup-2022-stats-api.herokuapp.com/`

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The API will return these error types when requests fail:

- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable

### Endpoints

#### GET /countries

- General:

  - Returns a dictionary of all available countries and success value.

- Sample: `curl https://world-cup-2022-stats-api.herokuapp.com/countries`

  ```json
  {
    "countries": [
      {
        "coach": "Lionel Scaloni",
        "id": 1,
        "name": "Argentina",
        "rank": 3
      },
      {
        "coach": "Tite",
        "id": 2,
        "name": "Brazil",
        "rank": 1
      },
      {
        "coach": "Didier Deschamps",
        "id": 3,
        "name": "France",
        "rank": 4
      },
      {
        "coach": "Roberto Martínez",
        "id": 4,
        "name": "Belgium",
        "rank": 2
      }
    ],
    "success": true,
    "total_countries": 4
  }
  ```

#### GET /countries/{country_id}

- General:

  - Returns a single country of the given ID if it exists and success value.

- Sample: `curl https://world-cup-2022-stats-api.herokuapp.com/countries/1`

  ```json
  {
    "country": {
      "coach": "Lionel Scaloni",
      "id": 1,
      "name": "Argentina",
      "rank": 3
    },
    "success": true
  }
  ```

#### POST /countries

- General:

  - Creates a new country. Returns the the created country and success value.

- `curl https://world-cup-2022-stats-api.herokuapp.com/countries -X POST -H "Content-Type: application/json" -d '{"name":"England","rank":8,"coach":"Gary Southgate"}'`

  ```json
  {
    "country": {
      "coach": "Gary Southgate",
      "id": 5,
      "name": "England",
      "rank": 8
    },
    "success": true
  }
  ```

#### PATCH /countries/{country_id}

- General:

  - Updates a country of the given ID if it exists. Returns the the updated country and success value.

- `curl https://world-cup-2022-stats-api.herokuapp.com/countries/3 -X POST -H "Content-Type: application/json" -d '{"rank":15,"coach":"Thomas Tuchel"}'`

  ```json
  {
    "country": {
      "coach": "Thomas Tuchel",
      "id": 3,
      "name": "France",
      "rank": 15
    },
    "success": true
  }
  ```

#### DELETE /countries/{country_id}

- General:
  - Deletes the country of the given ID if it exists. Returns the ID of the deleted country and success value.
- `curl -X DELETE https://world-cup-2022-stats-api.herokuapp.com/questions/4`

```json
{
  "success": true,
  "deleted": 4
}
```

#### GET /players

- General:

  - Returns a dictionary of all available players and success value.

- Sample: `curl https://world-cup-2022-stats-api.herokuapp.com/players`

  ```json
  {
    "players": [
      {
        "assists": 2,
        "country_id": 3,
        "goals": 8,
        "id": 1,
        "name": "Kylian Mbappe"
      },
      {
        "assists": 3,
        "country_id": 1,
        "goals": 7,
        "id": 2,
        "name": "Lionel Messi"
      },
      {
        "assists": 1,
        "country_id": 2,
        "goals": 2,
        "id": 3,
        "name": "Neymar"
      },
      {
        "assists": 1,
        "country_id": 1,
        "goals": 1,
        "id": 4,
        "name": "Alexis Mac Allister"
      }
    ],
    "success": true,
    "total_players": 4
  }
  ```

#### GET /players/{player_id}

- General:

  - Returns a single player of the given ID if it exists and success value.

- Sample: `curl https://world-cup-2022-stats-api.herokuapp.com/players/1`

  ```json
  {
    "player": {
      "assists": 2,
      "country_id": 3,
      "goals": 8,
      "id": 1,
      "name": "Kylian Mbappe"
    },
    "success": true
  }
  ```

#### POST /players

- General:

  - Creates a new player. Returns the the created player and success value.

- `curl https://world-cup-2022-stats-api.herokuapp.com/players -X POST -H "Content-Type: application/json" -d '{"name":"Richarlison","goals":3,"assists":0,"country_id":2}'`

  ```json
  {
    "player": {
      "name": "Richarlison",
      "goals": 3,
      "assists": 0,
      "country_id": 2
    },
    "success": true
  }
  ```

#### PATCH /players/{player_id}

- General:

  - Updates a player of the given ID if it exists. Returns the the updated player and success value.

- `curl https://world-cup-2022-stats-api.herokuapp.com/players/3 -X POST -H "Content-Type: application/json" -d '{"goals":10,"assists":5,"country_id":5}'`

  ```json
  {
    "player": {
      "name": "Kylian Mbappe",
      "goals": 10,
      "assists": 5,
      "country_id": 5
    },
    "success": true
  }
  ```

#### DELETE /players/{player_id}

- General:
  - Deletes the player of the given ID if it exists. Returns the ID of the deleted player and success value.
- `curl -X DELETE https://world-cup-2022-stats-api.herokuapp.com/players/4`

```json
{
  "success": true,
  "deleted": 4
}
```

## Built With

- [Python 3](https://www.python.org/) - The programming language used
- [Flask](https://palletsprojects.com/p/flask/) - The web framework used
- [Postgres](https://www.postgresql.org/) - Relational Database used
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - Database Migration manager
- [SQLAlchemy ORM](https://sqlalchemy.org/) - ORM library

## Authors

- **[Pemberai Sweto](https://github.com/thepembeweb)** - _Initial work_ - [2022 FIFA World Cup Stats Api](https://github.com/thepembeweb/2022-fifa-world-cup-stats-api)

## License

[![License](http://img.shields.io/:license-mit-green.svg?style=flat-square)](http://badges.mit-license.org)

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
- Copyright 2023 © [Pemberai Sweto](https://github.com/thepembeweb).
