from django.shortcuts import render_to_response, HttpResponse
from django.views.generic import ListView
from noticeboard.models import Notice


def testing_view(request):
    return HttpResponse("OK")


class NoticeBoardView(ListView):
    model = Notice
    template_name = 'noticeboard/index.html'
