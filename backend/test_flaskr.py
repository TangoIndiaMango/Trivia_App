import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = 'postgresql://{}:{}@{}/{}'.format('postgres', 'TIMMY', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)


        self.new_question = {
            'question': 'Which program did I attain this knowledge from',
            'answer': 'Udacity, Udemy, Canover, Flaskr',
            'difficulty': 2,
            'category': '4'
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_to_see_categories(self):

        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True),      
        self.assertTrue(data["categories"])

    def test_get_paginated_questions(self):
        response = self.client().get('/questions')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))


    def test_404_request_preceed_page(self):
        res = self.client().get('/question/160')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Question not found')


    
    def test_delete_question(self):

        # create a new question to be deleted
        question = Question(question=self.new_question['question'], answer=self.new_question['answer'],
                            category=self.new_question['category'], difficulty=self.new_question['difficulty'])
        question.insert()

        question_id = question.id

        ex_questions = Question.query.all()

        res = self.client().delete('/questions/{}'.format(question_id))
        data = json.loads(res.data)

        upcoming_questions = Question.query.all()

        question = Question.query.filter(Question.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], question_id)
        self.assertTrue(len(ex_questions) - len(upcoming_questions) == 1)
        self.assertEqual(question, None)




    def test_created_new_question(self):

        ex_questions = Question.query.all()

        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        upcoming_questions = Question.query.all()

        question = Question.query.filter_by(id=data['created']).one_or_none

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(upcoming_questions) - len(ex_questions) == 1)
        self.assertIsNotNone(question)



    def test_search_questions(self):
        """Tests search questions success"""

        response = self.client().post('/questions', json={'searchTerm': 'title'})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertEqual(len(data['questions']), 2)

        self.assertEqual(data['questions'][0]['id'], 5)

    def test_404_if_search_questions_fails(self):
        """Tests search questions failure 404"""
        res = self.client().post('/questions',json={'searchTerm': 'yzkpogr'})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Question not found')

    def test_get_questions_by_category(self):
        """Tests getting questions by category success"""

        response = self.client().get('/categories/2/questions')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertNotEqual(len(data['questions']), 0)

        self.assertEqual(data['current_category'], 'Art')

    def test_400_if_questions_by_category_fails(self):
        """Tests getting questions by category failure 400"""

        response = self.client().get('/categories/100/questions')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_play_quiz_game(self):
        """Tests playing quiz game success"""

        response = self.client().post('/quiz',json={'previous_questions': [20, 21], 'quiz_category': {'type': 'Art', 'id': '2'}})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertTrue(data['question'])

        self.assertEqual(data['question']['category'], 2)
        self.assertNotEqual(data['question']['id'], 20)
        self.assertNotEqual(data['question']['id'], 21)

    def test_play_quiz_fails(self):
        """Tests playing quiz game failure 400"""

        response = self.client().post('/quiz', json={})

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
