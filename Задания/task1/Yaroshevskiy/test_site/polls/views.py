from django.http import HttpResponse
from django.shortcuts import render
# from db_get_data import exec_query


def index(request):
    context = {
        "text": "test"
    }

    return HttpResponse(render(request, "polls/index.html", context))


def test(req):
    return HttpResponse("test")
