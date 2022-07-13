from django.contrib.auth.decorators import login_required
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


@login_required(login_url='login')
def question_create(request):
    profile = request.user.profile
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.owner = profile
            question.save()
            return redirect('questions_list')

    context = {'form': form}
    return render(request, 'community/question_forms.html', context)


@login_required(login_url='login')
def question_update(request, pk):
    profile = request.user.profile
    question = profile.question_set.get(id=pk)
    form = QuestionForm(instance=question)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('questions_list')

    context = {'form': form}
    return render(request, 'community/question_forms.html', context)


@login_required(login_url='login')
def question_delete(request, pk):
    profile = request.user.profile
    question = profile.question_set.get(id=pk)
    if request.method == "POST":
        question.delete()
        return redirect('questions_list')
    context = {'object': question}
    return render(request, 'community/question_delete.html', context)
