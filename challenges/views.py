from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat healthy for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Do yoga every week",
    "may": "Eat healthy for the entire month!",
    "june": "Walk for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Do yoga every week",
    "september": "Eat healthy for the entire month!",
    "october": "Walk for at least 20 minutes every day!",
    "november": "Learn Django for at least 20 minutes every day!",
    "december": "Do yoga every week"
}

# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list (monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
