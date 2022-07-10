from django import forms
from django.forms import ModelForm

from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'topic', 'content', 'owner']
        widgets = {

        }

    def __int__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.item():
            field.widgets.attrs.update({'class': 'input'})
        # self.fields['title'].widgets.attrs.update(
        #     {'class': 'post_name', 'id': 'post_name', 'name': 'post_name', 'rows': '1', 'col': '50', 'placeholder': 'Title...'})
