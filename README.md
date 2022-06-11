# Full Stack Trivia API Project

This project is a game where users can test their knowledge answering trivia questions. The task for the project was to create an API and test suite for implementing the following functionality:
Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
Delete questions.
Add questions and require that they include question and answer text.
Search for questions based on a text query string.
Play the quiz game, randomizing either all questions or within a specific category.

## Getting Started

### Install Dependencies
Installing Dependencies
Developers using this project should already have Python3, pip, node, and npm installed.

Frontend Dependencies
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the frontend directory of this repository. After cloning, open your terminal and run:
```
npm install
```
Backend Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:
```
pip install -r requirements.txt
```
Running the Frontend in Dev Mode
The frontend app was built using create-react-app. In order to run the app in development mode use npm start. You can change the script in the package.json file.

Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.
```
npm start
```
- **Running the Server** 
From within the backend directory first ensure you are working using your created virtual environment.

#### Preview of some Key Programs for the Project

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createbd trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

NOTE: 
- export FLASK_APP=flaskr
- export FLASK_ENV=development
- python flaskr.py

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

## Testing

To run the tests, run or
To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
Omit the dropdb command the first time you run tests.
```
## API Reference
### Getting Started
- Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
- Authentication: This version does not require authentication or API keys.

#### Error Handling
Errors are returned as JSON in the following format:
```
{
    "success": False,
    "error": 404,
    "message": "Question not found"
}

```
The API will return three types of errors:
```
- 400 – bad request
- 404 – Question not found
- 422 – unprocessable
```
## Endpoints
GET /categories
- General: Returns a list categories.

- Sample: curl http://127.0.0.1:5000/categories
```sh
  {
      "categories": {
          "1": "Science", 
          "2": "Art", 
          "3": "Geography", 
          "4": "History", 
          "5": "Entertainment", 
          "6": "Sports"
      }, 
      "success": true
  }
  ```

#### GET /questions
- General:

 `-- Returns a list questions.`
 `-- Results are paginated in groups of 10.`
 `-- Also returns list of categories and total number of questions.`
 - Sample: ``` sh curl http://127.0.0.1:5000/questions ```
``` sh
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
              "answer": "Udacity, Udemy, Canover, Flaskr", 
              "category": 2, 
              "difficulty": 4, 
              "id": 16, 
              "question": "Which program did I attain this knowledge from?"
          }, 
          {
              "answer": "Muhammad Ali", 
              "category": 4, 
              "difficulty": 1, 
              "id": 9, 
              "question": "What boxer's original name is Cassius Clay?"
          }, 
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
              "answer": "Edward Scissorhands", 
              "category": 5, 
              "difficulty": 3, 
              "id": 6, 
              "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
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
      "total_questions": 19
  }
  ```

#### DELETE /questions/<int:id>
- General:

> Deletes a question by id using url parameters.
> Returns id of deleted question upon success.
- Sample: ```sh curl -X DELETE http://127.0.0.1:5000/questions/6 ```
```
  {
      "deleted": 6, 
      "success": true
  }
```

#### POST /questions
This endpoint either creates a new question or returns search results.

1. If no search term is included in request:
- General:

  > Creates a new question using JSON request parameters.
  > Returns JSON object with newly created question, as well as paginated questions.
  - Sample: ```sh curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{ "question": "Which program did I attain this knowledge from?", "answer": "Udacity", "difficulty": 2, "category": "4" }'```
``` sh
  {
      "created": 173, 
      "question_created": "Which US state contains an area known as the Upper Penninsula?", 
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
          }, 
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
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          }
      ], 
      "success": true, 
      "total_questions": 20
  }
  ```

If search term **is** included in request:
- General:

> Searches for questions using search term in JSON request parameters.
> Returns JSON object with paginated matching questions.
- Sample: ```sh curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "title"}' ```
```
  {
      "questions": [
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
              "answer": "The Palace of Versailles", 
              "category": 3, 
              "difficulty": 3, 
              "id": 14, 
              "question": "In which royal palace would you find the Hall of Mirrors?"
          }, 
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
              "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
          }, 
          {
              "answer": "Jackson Pollock", 
              "category": 2, 
              "difficulty": 2, 
              "id": 19, 
              "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
          }, 
          {
              "answer": "Scarab", 
              "category": 4, 
              "difficulty": 4, 
              "id": 23, 
              "question": "Which dung beetle was worshipped by the ancient Egyptians?"
          }, 
          {
              "answer": "Michigan", 
              "category": 3, 
              "difficulty": 3, 
              "id": 173, 
              "question": "Which US state contains an area known as the Upper Penninsula?"
          }
      ], 
      "success": true, 
      "total_questions": 18
  }
  ```
#### GET /categories/<int:id>/questions
- General:

> Gets questions by category id using url parameters.
> Returns JSON object with paginated matching questions.
- Sample: ```sh curl http://127.0.0.1:5000/categories/1/questions```
```
  {
      "current_category": "Science", 
      "questions": [
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
          }
      ], 
      "success": true, 
      "total_questions": 18
  }
```

#### POST /quiz
- General:

>Allows users to play the quiz game.
>Uses JSON request parameters of category and previous questions.
>Returns JSON object with random question not among previous questions.

- Sample: ```sh curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [20, 21], "quiz_category": {"type": "Science", "id": "1"}}' ```
```
  {
      "question": {
          "answer": "Blood", 
          "category": 1, 
          "difficulty": 4, 
          "id": 22, 
          "question": "Hematology is a branch of medicine involving the study of what?"
      }, 
      "success": true
  }
  ```

### Authors
Alex Sandberg-Bernard authored the API (__init__.py), test suite (test_flaskr.py), and this README.
All other project files, including the models and frontend, were created by Udacity as a project template for the Full Stack Web Developer Nanodegree.