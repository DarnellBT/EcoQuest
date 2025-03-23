"""Module contains logic for quiz app"""
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Question, Quiz, QuizCompleted
from registration.models import UserProfile


# pylint: disable=line-too-long

def quiz(request, id):
    """
    Handles the quiz page logic.
    Dynamically changes content based on the quiz ID.
    Tracks user progress, calculates points, and prevents reattempts.
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    # retrieves quiz record and userprofile record
    quiz_obj = Quiz.objects.get(quizId=id)
    user_obj = UserProfile.objects.get(userId=request.user.id).user
    # checks if the quiz has been completed by the user before 
    quiz_completed_record = QuizCompleted.objects.filter(quiz=quiz_obj, user=user_obj)
    print("Completed:", quiz_completed_record.exists())
    if quiz_completed_record.exists() == True:
        messages.error(request, "You have already completed this quiz")
        return redirect("../../../map/")
    else: 
        pass

    all_questions = Question.objects.filter(quiz=quiz_obj)
    all_questions = list(all_questions)
    
    
    # initialises variables 
    choices = []
    question_index = request.session.get('question_index', 0)
    user_points = request.session.get('user_points', 0)
    question_number = question_index + 1
    questions = []
    correct_answers = []
    question_points = []
    submitted_answers = []
    # puts questions, choices, answer, points into correct arrays 
    for initialise_data in all_questions:
        questions.append(initialise_data.question)
        question_choices = [initialise_data.choice1, initialise_data.choice2, initialise_data.choice3, initialise_data.choice4]
        choices.append(question_choices)
        correct_answers.append(initialise_data.answer)
        question_points.append(initialise_data.points)
    
    if request.method == 'POST':
        # retrieves current session vwriables of user and if doesnt exist, sets it to 0 or the default list 
        index_post = request.session.get('question_index', 0)
        questions_post = request.session.get('questions', questions)
        choices_post = request.session.get('choices', choices)
        
        user_choice = request.POST.get("question")
        # sets submitted session to the user choice 
        request.session['submitted'].append(user_choice)
       
        all_questions_choices = Question.objects.filter(quiz=quiz_obj)
        all_questions_choices = list(all_questions_choices)
  
        # sets user points in session (change so user points are reset in results after being used)
        # send question, user answer, correct answer
        # records amount of points user has gotten, total correct answers 
        if request.session['answers'][index_post] == user_choice:
            question_point = request.session['points'][index_post]
            request.session['user_points'] += question_point
            request.session['correct_total'] += 1
        else:
            pass
        
        # increments questioj index for use to get correct question, answer, choice and points 
        request.session['question_index'] = index_post + 1
        request.session.modified = True
        # if end of quiz, session is reset 
        if request.session['question_index'] >= len(questions_post):
            request.session['question_index'] = 0  
            request.session['points'] = 0
            request.session['choices'] = []
            quiz_obj = Quiz.objects.get(quizId=id)
            # create quizcompleted record so user cannot redo quiz
            user_obj = (UserProfile.objects.get(userId=request.user.id)).user
            QuizCompleted.objects.create(user=user_obj, quiz=quiz_obj, completed=True)
            return redirect('./results')
        # incremenet question number for html vwribale and get index to use 
        question_number = request.session['question_index'] + 1
        index_post = request.session['question_index']
        # send these variables to html frontend 
        context = {
            'question_index': index_post,
            'question_number': question_number,
            'question': questions_post[index_post],
            'choice1': choices_post[index_post][0],
            'choice2': choices_post[index_post][1],
            'choice3': choices_post[index_post][2],
            'choice4': choices_post[index_post][3],
            'total_number': len(questions_post),
            'user_auth': request.user,
            'userprofile': user_obj,
        }
        return render(request, 'quiz.html', context)
    # set user session with these variables 
    request.session['question_index'] = question_index   
    request.session['questions'] = questions
    request.session['choices'] = choices
    request.session['answers'] = correct_answers
    request.session['points'] = question_points
    request.session['user_points'] = user_points
    request.session['submitted'] = submitted_answers
    request.session['correct_total'] = 0
   

    context = {
        'question_index': question_index,
        'question_number': question_number,
        'question': questions[question_index],
        'choice1': choices[question_index][0],
        'choice2': choices[question_index][1],
        'choice3': choices[question_index][2],
        'choice4': choices[question_index][3],
        'total_number': len(questions),
        'user_auth': request.user,
        'userprofile': user_obj,
    }
    return render(request, 'quiz.html', context)

def results(request, id):
    """
    Handles the results page logic.
    Displays the user's score, correct answers, and updates their points.
    Resets session variables after the quiz is completed.
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    
    # retrieves session info 
    userProfile = UserProfile.objects.get(userId=request.user.id)
    points = request.session['user_points']
    total_correct = request.session['correct_total']
    total_questions =  len(request.session['questions'])
    # give points to user
    total_points = userProfile.points + points
    userProfile.points = total_points
    userProfile.save()
    
    submitted_user_answers = request.session['submitted']
    correct_question_answers = request.session['answers']
    quiz_questions = request.session['questions']
    submitted_answers = []
    for i in range(0, total_questions):
        submitted_list = []
        submitted_list.append(i+1)
        submitted_list.append(quiz_questions[i])
        submitted_list.append(submitted_user_answers[i])
        submitted_list.append(correct_question_answers[i])
        submitted_answers.append(submitted_list)   
    # reset session for user to start another question
    request.session['user_points'] = 0
    request.session['questions'] = []
    request.session['submitted'] = []
    request.session['correct_total'] = 0
    request.session['answers'] = []

   
    context = {
        'score': total_correct,
        'total': total_questions,
        'current_points': total_points,
        'submitted_answers': submitted_answers,
        'user_auth': request.user,
        'userprofile': userProfile,
    }
    return render(request, 'submitQuiz.html', context)
