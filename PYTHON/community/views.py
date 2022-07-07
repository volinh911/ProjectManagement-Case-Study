from django.shortcuts import render, redirect

from .forms import QuestionForm
from .models import Question

QUESTION_TOPIC = (
    ('English', 'English'),
    ('Mandarin', 'Mandarin'),
    ('German', 'German'),
)


# Create your views here.
def questions_list(request):
    questions = Question.objects.all().order_by('-date_created')
    topics = QUESTION_TOPIC
    return render(request, 'community/questions_list.html', {'questions': questions, 'topics': topics})


def question_detail(request, pk):
    # replies = Reply.objects.get(questionID=pk)
    question = Question.objects.get(id=pk)
    return render(request, 'community/question_detail.html', {'question': question})


def question_create(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions_list')

    context = {'form': form}
    return render(request, 'community/question_forms.html', context)


def question_update(request, pk):
    question = Question.objects.get(id=pk)
    form = QuestionForm(instance=question)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions_list')

    context = {'form': form}
    return render(request, 'community/question_forms.html', context)


def question_delete(request, pk):
    question = Question.objects.get(id=pk)
    if request.method == "POST":
        question.delete()
        return redirect('questions_list')
    context = {'object': question}
    return render(request, 'community/question_delete.html', context)
