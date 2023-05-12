from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "text": "test",
        "list": [0, 1, 2, 3, "frogg"]
    }

    return HttpResponse(render(request, "polls/index.html", context))
