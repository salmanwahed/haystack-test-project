from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def testing_view(request):
    return render_to_response('noticeboard/index.html')
