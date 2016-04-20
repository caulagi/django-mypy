import typing  # noqa

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Question


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-id')[:5]


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    if not request.user.has_permission('read'):
        return None
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
