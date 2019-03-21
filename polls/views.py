from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from polls.models import Question
from django.template import loader
from django.shortcuts import render
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .tests import creat_question
from django.test import TestCase


# from django import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    #@property
    def get_queryset(self):

        #return Question.objects.order_by('-pub_date')
        # if not request.user.is_authenticated:
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    #def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    class QuestionDetailViewTests(TestCase):
        """检查是否访问未到时间问卷"""

        def test_future_question(self):
            future_question = creat_question(question_text='Future question. ', days=5)
            url = reverse('polls:detail', args=(future_question.id,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

        def test_past_question(self):
            past_question = create_question(question_text='Past Question. ', days=5)
            url = reverse('polls:detail', args=(past_question.id,))
            response = self.client.get(url)
            self.assertEqual(response, past_question.question_text)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # return HttpResponse("请为问卷%s提交你的答案。" % question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "还没有选择。", })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
