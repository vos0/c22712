from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render, redirect
from django.urls import reverse

from .models import Question, Choice, UserVariant
from datetime import datetime

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_success.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def user_profile(request):
    context = {
       "user": request.user
    }
    return render(request, 'user_profile.html', context)

def menu(request):
    return render(request, 'Меню.html')

def votes(request):
    return render(request, 'Голосования.html')

def index(request):
    questions_list = Question.objects.order_by('-pub_date')[:5]
    context = dict(
        user = request.user,
        questions = questions_list
    )
    return render(request, 'index.html', context)

def results(request):
    return render(request, 'results.html')

def get(request, id):
    question = Question.objects.get(id=id)
    answers = list(Choice.objects.filter(question=question).values('id', 'choice_text'))
    for i, ans in enumerate(answers):
        user_answers = list(UserVariant.objects.filter(choice_id=ans['id']).values_list('user_id', flat=True))
        answers[i]['count'] = len(user_answers)
        if request.user.id in user_answers:
            answers[i]['target'] = True
        else:
            answers[i]['target'] = False

        context = dict(
            user=request.user,
            question=question,
            answers=answers
        )
    return render(request, 'Vote.html', context)

def submit(request, id):
    voting = Question.objects.get(id=id)
    if request.method == 'POST':
        variant = request.POST.get('variant') or None
        user_variants = UserVariant.objects.filter(user=request.user, choice__question_id=voting.id)
        user_variant = user_variants.first() or None
        if user_variant:
            user_variant.variant_id = variant
        elif variant:
            user_variant = UserVariant(user=request.user, choice_id=variant)
        if user_variant:
            user_variant.save()
    return redirect(reverse('list-votings'))
"""
def vote(request):
    question = get_list_or_404(Question)
    for q in question:
        try:
            selected_choice = q.choice_set.get(pk = request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'results.html', {
                'question': q,
                'error_message': "Вы ничего не выбрали",
            })
        else:
            selected_choice.update(votes=F('votes') + 1)
    return render(request, 'results.html', context)
"""
def putin(request):
    return render(request, 'Путин.html')

def cyberpunk(request):
    return render(request, 'Cyberpunk.html')

def thanks(request):
    return render(request, 'Спасибо.html')