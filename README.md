# 2022 FIFA World Cup Stats Api

> The 2022 FIFA World Cup Stats Api demonstrates role-based access for data capture supervisors, reviewers, capturers as well as the general public to administer and view player statistics from the 2022 FIFA World Cup hosted in Qatar.

![](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)

![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)


## 2022 FIFA World Cup Stats Api URL

Visit the website [https://world-cup-2022-stats-api.herokuapp.com](https://world-cup-2022-stats-api.herokuapp.com/)

## Overview

The application showcases the following features:

* Display player statistics.
* Add, edit and delete player statistics.
* Display countries participating in the world cup.
* Add, edit and delete countries.
* Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
* DRY (don't repeat yourself) principles of class and method design.
* Working with modules and packages in Python.
* Coding best practices for style and documentation
* Ensuring that code, docstrings, and comments adhere to [PEP 8 Standards](https://www.python.org/dev/peps/pep-0008/).


## Installation

### Requirements
The project requires `pip` installed.

If you do not have `pip` installed, you can download it here: [pip](https://pip.pypa.io/en/stable/installing/)

### Setup

1. **Create an empty database (fifa-wc) in postgres locally:
```sh
$ createdb -U postgres fifa-wc
```

2. **Create an empty test database (fifa-wc_test) in postgres locally:
```sh
$ createdb -U postgres fifa-wc_test
```

3. **Clone the source locally:
```sh
$ git clone https://github.com/thepembeweb/2022-fifa-world-cup-stats-api.git
```

4. **Navigate to the application folder:
```sh
$ cd 2022-fifa-world-cup-stats-api
```

5. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

6. **Install project dependencies:
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


9. **Testing:

To deploy the tests, run

```bash
dropdb fifa-wc_test
createdb fifa-wc_test
psql fifa-wc_test < fifa-wc_test.psql
python test_app.py
```


## API Reference

### Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

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

- Sample: `curl http://127.0.0.1:5000/countries`

  ```json
  {
    "countries": [
      "1": "Science", 
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

#### GET /questions

- General:

  - Returns a list of questions, number of total questions and categories.
  - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

- Sample: `curl http://127.0.0.1:5000/questions` or `curl http://127.0.0.1:5000/questions?page=1`

  ```json
  {
    "categories": {
      "1": "Science", 
      "2": "Art", 
      "3": "Geography", 
      "4": "History", 
      "5": "Entertainment", 
      "6": "Sports"
    }, 
    "questions": [
      {
        "answer": "Apollo 13", 
        "category": 5, 
        "difficulty": 4, 
        "id": 2, 
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      }, 
      {
        "answer": "Tom Cruise", 
        "category": 5, 
        "difficulty": 4, 
        "id": 4, 
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      }, 
      {
        "answer": "Maya Angelou", 
        "category": 4, 
        "difficulty": 2, 
        "id": 5, 
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      }, 
      {
        "answer": "Edward Scissorhands", 
        "category": 5, 
        "difficulty": 3, 
        "id": 6, 
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      }, 
      {
        "answer": "Muhammad Ali", 
        "category": 4, 
        "difficulty": 1, 
        "id": 9, 
        "question": "What boxer's original name is Cassius Clay?"
      }, 
      {
        "answer": "Brazil", 
        "category": 6, 
        "difficulty": 3, 
        "id": 10, 
        "question": "Which is the only team to play in every soccer World Cup tournament?"
      }, 
      {
        "answer": "Uruguay", 
        "category": 6, 
        "difficulty": 4, 
        "id": 11, 
        "question": "Which country won the first ever soccer World Cup in 1930?"
      }, 
      {
        "answer": "George Washington Carver", 
        "category": 4, 
        "difficulty": 2, 
        "id": 12, 
        "question": "Who invented Peanut Butter?"
      }, 
      {
        "answer": "Lake Victoria", 
        "category": 3, 
        "difficulty": 2, 
        "id": 13, 
        "question": "What is the largest lake in Africa?"
      }, 
      {
        "answer": "The Palace of Versailles", 
        "category": 3, 
        "difficulty": 3, 
        "id": 14, 
        "question": "In which royal palace would you find the Hall of Mirrors?"
      }
    ], 
    "success": true, 
    "total_questions": 20
  }
  ```

#### POST /questions

- General:

  - Creates a new question using the submitted question, answer, difficulty and category. Returns the ID of the created question, success value, total questions, and question list based on current page number to update the frontend.

- `curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type: application/json" -d '{"question":"Test Question","answer":"Test Answer","difficulty":1,"category":"3"}'`

  ```json
  {
    "created": 28,
    "questions": [
      {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      },
      {
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4,
        "id": 4,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
      },
      {
        "answer": "Maya Angelou",
        "category": 4,
        "difficulty": 2,
        "id": 5,
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },
      {
        "answer": "Edward Scissorhands",
        "category": 5,
        "difficulty": 3,
        "id": 6,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
      },
      {
        "answer": "Muhammad Ali",
        "category": 4,
        "difficulty": 1,
        "id": 9,
        "question": "What boxer's original name is Cassius Clay?"
      },
      {
        "answer": "Brazil",
        "category": 6,
        "difficulty": 3,
        "id": 10,
        "question": "Which is the only team to play in every soccer World Cup tournament?"
      },
      {
        "answer": "Uruguay",
        "category": 6,
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
      },
      {
        "answer": "George Washington Carver",
        "category": 4,
        "difficulty": 2,
        "id": 12,
        "question": "Who invented Peanut Butter?"
      },
      {
        "answer": "Lake Victoria",
        "category": 3,
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?"
      },
      {
        "answer": "The Palace of Versailles",
        "category": 3,
        "difficulty": 3,
        "id": 14,
        "question": "In which royal palace would you find the Hall of Mirrors?"
      }
    ],
    "success": true,
    "total_questions": 24
  }
  ```

#### DELETE /questions/{question_id}

- General:
  - Deletes the question of the given ID if it exists. Returns the ID of the deleted question, success value, total questions, and question list based on current page number to update the frontend.
- `curl -X DELETE http://127.0.0.1:5000/questions/23`

```json
{
  "deleted": 23,
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```


## Built With

* [Python 3](https://www.python.org/) - The programming language used
* [Flask](https://palletsprojects.com/p/flask/) - The web framework used
* [Postgres](https://www.postgresql.org/) - Relational Database used
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - Database Migration manager
* [SQLAlchemy ORM](https://sqlalchemy.org/) - ORM library


## Authors

* **[Pemberai Sweto](https://github.com/thepembeweb)** - *Initial work* - [2022 FIFA World Cup Stats Api](https://github.com/thepembeweb/2022-fifa-world-cup-stats-api)

## License

[![License](http://img.shields.io/:license-mit-green.svg?style=flat-square)](http://badges.mit-license.org)

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
- Copyright 2023 © [Pemberai Sweto](https://github.com/thepembeweb).

