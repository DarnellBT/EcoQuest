"""Module contains logic for quiz app"""
from django.contrib import messages
from django.shortcuts import render, redirect
from registration import models as register_models

from .models import Question


# pylint: disable=line-too-long

def quiz(request, id):
    """Function contains quiz page logic, dynamically changes content via id"""
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    # retrieves all columns neccessary to fill the form
    all_questions = Question.objects.filter(quizId=id).values('question', 'choice1', 'choice2', 'choice3', 'choice4')
    # convert the dict into a iterable format
    all_questions = list(all_questions)
    if request.method == 'POST':
        # retrieve all objects, number of questions, default score and new dict
        questions = Question.objects.all()
        score = 0
        total_questions = Question.objects.all().count()
        print("Count: ", total_questions)
        submitted = {}
        current_user = request.user
        current_user_id = current_user.id
        user_profile = register_models.UserProfile.objects.get(userId=current_user_id)
        print(user_profile)
        user_points = user_profile.points
        num = 1
        # get user answer and compare with form submission and add marks as appropriate
        for question in questions:
            user_answer = request.POST.get(f"question_{num}")
            submitted[question.questionId] = user_answer
            print(user_answer)
            num += 1
            if user_answer == question.answer:
                score += 1
                question_points = question.points
                user_points += question_points
        user_profile.points = user_points
        user_profile.save()
        # Send information to html page
        context = {
            'score': score,
            'current_points': user_points,
            'total': total_questions,
            'submitted_answers': submitted,
            'questions': questions,
        }

        return render(request, 'submitQuiz.html', context)
    return render(request, 'quiz.html', {'questions': all_questions})
