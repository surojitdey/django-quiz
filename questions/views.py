from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .helper import Quiz

def quiz(request):
  quiz = Quiz()
  country = quiz.get_random_country_name()
  context = {
    "country": country
  }
  if request.method == "POST":
    previous_country = request.POST.get("country")
    given_answer = request.POST.get("answer")
    correct_answer = quiz.get_correct_capital(previous_country)
    context["previous_country"] = previous_country
    context["given_answer"] = given_answer
    context["correct_answer"] = correct_answer
  return render(request, 'base.html', context)