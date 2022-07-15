from django.forms import ModelForm

from .models import Question, Reply


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'topic', 'content']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
