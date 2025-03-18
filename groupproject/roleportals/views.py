from django.shortcuts import render, redirect, get_object_or_404
from challenge.models import Challenge, ChallengeCompleted, ChallengeImages
from django.contrib.auth.models import User
from registration.models import UserProfile
from map.models import Location
from django.contrib import messages
from quiz.models import Quiz, Question
from .forms import LocationForm, ChallengeForm, QuestionForm, QuizForm

def admin_portal(request):
    user_profile = UserProfile.objects.get(userId=request.user.id)

    if user_profile.is_admin:
        pass
    elif user_profile.is_game_keeper:
        messages.error(request, 'You do not have access!')
    else: 
        messages.error(request, 'You do not have access!')
    return render(request, 'admin_page.html', {'user_auth':user_profile.user})

def gamekeeper_portal(request):
    user_profile = UserProfile.objects.get(userId=request.user.id)

    if user_profile.is_admin:
        pass
    elif user_profile.is_game_keeper:
        pass
    else: 
        messages.error(request, 'You do not have access!')
        return redirect("../home/")
   


    all_entries = ChallengeImages.objects.all()
    all_info = []

    if len(all_entries) > 0:
        for entry in all_entries:
            info = []
            info.append(entry.user.id)
            info.append(entry.challenge.challenge)
            info.append(entry.image.url)
            info.append(entry.challenge.points)
            info.append(entry.imageId)
        all_info.append(info)

        if request.method == 'POST':
            userId = request.POST.get("userId")
            challenge_info = request.POST.get("challenge")
            rejected = request.POST.get(f"rejected_{userId}_{challenge_info}")
            approved = request.POST.get(f"approved_{userId}_{challenge_info}")
            imageId = request.POST.get("imageId")
    
            if approved:
                challenge = Challenge.objects.get(challenge=challenge_info)
                user_profile = UserProfile.objects.get(userId=userId)
                ChallengeCompleted.objects.create(userId=user_profile, challengeId=challenge, completed=True)
                ChallengeImages.objects.filter(imageId=imageId).delete()
                challenge_points = challenge.points
                user_profile.points += challenge_points
                user_profile.save()

                return redirect("./")
            if rejected:
                return redirect("./")

        context = {
        'info':all_info,
        }
        return render(request, "game_keeper.html", context)
    else:
        return render(request, "game_keeper.html")




def admin_location(request):
    locations = Location.objects.all()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = LocationForm()
    return render(request, 'admin_location.html', {'locations': locations, 'form': form})

def edit_location(request, location_id):
    location = get_object_or_404(Location, locationId=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('../../')
    else:
        form = LocationForm(instance=location)
    return render(request, 'edit_location.html', {'form': form})

def delete_location(request, location_id):
    location = get_object_or_404(Location, locationId=location_id)
    location.delete()
    return redirect('../../')




def admin_quiz(request):
    quizzes = Quiz.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = QuizForm()
    return render(request, 'admin_quiz.html', {'quizzes': quizzes, 'form': form})

def edit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, quizId=quiz_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('../../')
    else:
        form = QuizForm(instance=quiz)
    return render(request, 'edit_quiz.html', {'form': form})

def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, quizId=quiz_id)
    quiz.delete()
    return redirect('../../')






def edit_location(request, location_id):
    location = get_object_or_404(Location, locationId=location_id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('../../')
    else:
        form = LocationForm(instance=location)
    return render(request, 'edit_location.html', {'form': form})

def delete_location(request, location_id):
    location = get_object_or_404(Location, locationId=location_id)
    location.delete()
    return redirect('../../')





def admin_question(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = QuestionForm()
    return render(request, 'admin_question.html', {'questions': questions, 'form': form})
   


def edit_question(request, question_id):
    question = get_object_or_404(Question, questionId=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('../../')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'edit_question.html', {'form': form})

def delete_question(request, question_id):
    question = get_object_or_404(Question, questionId=question_id)
    question.delete()
    return redirect('../../')





def admin_challenge(request):
    challenges = Challenge.objects.all()
    if request.method == 'POST':
        form = ChallengeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form = ChallengeForm()
    return render(request, 'admin_challenge.html', {'challenges': challenges, 'form': form})
    


def edit_challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, challengeId=challenge_id)
    if request.method == 'POST':
        form = ChallengeForm(request.POST, instance=challenge)
        if form.is_valid():
            form.save()
            return redirect('../../')
    else:
        form = ChallengeForm(instance=challenge)
    return render(request, 'edit_challenge.html', {'form': form})

def delete_challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, challengeId=challenge_id)
    challenge.delete()
    return redirect('../../')



