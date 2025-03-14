"""Module contains test cases for quiz"""
from django.test import TestCase
from django.urls import reverse
from .models import Quiz, Question


def setup_account(instance):
    """Sets up a user account for testing."""
    # Registers user.
    register_form_data = {
        'username': 'Dragonite',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'JohnDoe@email.com',
        'password1': 'secret_pass',
        'password2': 'secret_pass'
    }
    instance.client.post('/register/', register_form_data)
    form_data = {
        'username': 'JohnDoe@email.com',
        'password': 'secret_pass'
    }
    instance.client.post('/login/', form_data)


class QuizModelTest(TestCase):
    """Class contains tests that use assert to test quiz models."""

    def test_create_quiz(self):
        """Test creating a Quiz instance"""
        # Creates a quiz instance.
        quiz = Quiz.objects.create(
            name='Test quiz name'
        )
        self.assertEqual(quiz.quizId, 1)
        self.assertEqual(quiz.name, 'Test quiz name')

    def test_create_question(self):
        """Test creating a Question instance"""
        # Creates a Quiz instance.
        quiz = Quiz.objects.create(
            name='Test quiz name'
        )
        # Creates a Question instance.
        question = Question.objects.create(
            quizId=quiz.quizId,
            question='This is a test question.',
            choice1='This is a test choice 1.',
            choice2='This is a test choice 2.',
            choice3='This is a test answer.',
            choice4='This is a test choice 4.',
            answer='This is a test answer.',
            points=10
        )
        self.assertEqual(question.questionId, 1)
        self.assertEqual(question.quizId, 1)
        self.assertEqual(question.question, 'This is a test question.')
        self.assertEqual(question.choice1, 'This is a test choice 1.')
        self.assertEqual(question.choice2, 'This is a test choice 2.')
        self.assertEqual(question.choice3, 'This is a test answer.')
        self.assertEqual(question.choice4, 'This is a test choice 4.')
        self.assertEqual(question.answer, 'This is a test answer.')
        self.assertEqual(question.points, 10)


class QuizViewTest(TestCase):
    """Class contains tests for quiz views."""

    def test_quiz_page_loads(self):
        """Test if the quiz page loads successfully"""
        # Creates a Quiz instance.
        quiz = Quiz.objects.create(
            name='Test quiz name'
        )
        # Creates a Question instance.
        Question.objects.create(
            quizId=quiz.quizId,
            question='This is a test question.',
            choice1='This is a test choice 1.',
            choice2='This is a test choice 2.',
            choice3='This is a test answer.',
            choice4='This is a test choice 4.',
            answer='This is a test answer.',
            points=10
        )
        setup_account(self)
        response = self.client.get(reverse('quiz', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        # Check we get quiz template.
        self.assertTemplateUsed(response, 'quiz.html')

    def test_results_page_loads(self):
        """Test if the results page loads successfully"""
        # Creates a Quiz instance.
        quiz = Quiz.objects.create(
            name='Test quiz name'
        )
        # Creates a Question instance.
        Question.objects.create(
            quizId=quiz.quizId,
            question='This is a test1 question.',
            choice1='This is a test1 choice 1.',
            choice2='This is a test1 choice 2.',
            choice3='This is a test1 answer.',
            choice4='This is a test1 choice 4.',
            answer='This is a test1 answer.',
            points=10
        )
        Question.objects.create(
            quizId=quiz.quizId,
            question='This is a test2 question.',
            choice1='This is a test2 choice 1.',
            choice2='This is a test1 choice 2.',
            choice3='This is a test2 answer.',
            choice4='This is a test2 choice 4.',
            answer='This is a test2 answer.',
            points=5
        )
        setup_account(self)
        # Must get the quiz page first to initialise session data.
        self.client.get(reverse('quiz', kwargs={'id': 1}))
        question1_form_data = {
            'question': ['This is a test1 answer.'],
        }
        question1_response = self.client.post(reverse('quiz', kwargs={'id': 1}), question1_form_data)
        self.assertEqual(question1_response.status_code, 200)
        self.assertTemplateUsed(question1_response, 'quiz.html')
        question2_form_data = {
            'question': ['This is a test2 answer.'],
        }
        question2_response = self.client.post(reverse('quiz', kwargs={'id': 1}), question2_form_data)
        results_response = self.assertRedirects(question2_response, '/quiz/1/results', status_code=302, target_status_code=301, fetch_redirect_response=True)
        # Check we get submitQuiz template.
        self.assertTemplateUsed(results_response, 'submitQuiz.html')

    def test_login_page_redirect_loads_if_not_logged_in(self):
        """Test if the login page loads successfully if a user is not logged in."""
        # Creates a Quiz instance.
        quiz = Quiz.objects.create(
            name='Test quiz name'
        )
        # Creates a Question instance.
        Question.objects.create(
            quizId=quiz.quizId,
            question='This is a test question.',
            choice1='This is a test choice 1.',
            choice2='This is a test choice 2.',
            choice3='This is a test answer.',
            choice4='This is a test choice 4.',
            answer='This is a test answer.',
            points=10
        )
        response = self.client.get(reverse('quiz', kwargs={'id': 1}))
        login_response = self.assertRedirects(response, '/login', status_code=302, target_status_code=301, fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')
