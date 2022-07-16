from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from vote.models import UP, DOWN

from .forms import QuestionForm, ReplyForm
from .models import Question, Reply

QUESTION_TOPIC = (
    ('English', 'English'),
    ('Mandarin', 'Mandarin'),
    ('German', 'German'),
)


# Create your views here.
def questions_list(request):
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')

    questions = Question.objects.filter(topic__icontains=search).order_by('-vote_score')
    topics = QUESTION_TOPIC
    return render(request, 'community/questions_list.html', {'questions': questions, 'topics': topics})


def question_detail(request, pk):
    question = Question.objects.get(id=pk)
    reply = question.reply_set.all().order_by('-vote_score')
    userID = request.user.id
    user = request.user
    form = ReplyForm()

    questionCheck = ''
    if question.votes.exists(userID, action=UP):
        questionCheck = 'up'
    elif question.votes.exists(userID, action=DOWN):
        questionCheck = 'down'

    replyDict = {}
    for comment in reply:
        print(comment.id)
        if comment.votes.exists(userID, action=UP):
            replyDict[comment.id] = 'up'
        elif comment.votes.exists(userID, action=DOWN):
            replyDict[comment.id] = 'down'

    print(replyDict)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        else:

            if request.POST.get('voteUp') == 'up':  # neu nguoi dung vote up
                if question.votes.exists(userID, action=UP):  # kiem tra nguoi dung co vote up chua
                    question.votes.delete(userID)
                    return redirect('question_detail', pk)
                else:
                    question.votes.up(userID)
                    return redirect('question_detail', pk)

            elif request.POST.get('voteDown') == 'down':  # neu nguoi dung vote down
                if question.votes.exists(userID, action=DOWN):  # kiem tra nguoi dung co vote down chua
                    question.votes.delete(userID)
                    return redirect('question_detail', pk)
                else:
                    question.votes.down(userID)
                    return redirect('question_detail', pk)

            elif request.POST.get('voteUpComment'):
                replyObj = Reply.objects.get(id=request.POST.get('voteUpComment'))
                if replyObj.votes.exists(userID, action=UP):
                    replyObj.votes.delete(userID)
                    return redirect('question_detail', pk)
                else:
                    replyObj.votes.up(userID)
                    return redirect('question_detail', pk)

            elif request.POST.get('voteDownComment'):
                replyObj = Reply.objects.get(id=request.POST.get('voteDownComment'))
                if replyObj.votes.exists(userID, action=DOWN):
                    replyObj.votes.delete(userID)
                    return redirect('question_detail', pk)
                else:
                    replyObj.votes.down(userID)
                    return redirect('question_detail', pk)

            else:
                form = ReplyForm(request.POST)
                if form.is_valid():
                    reply = form.save(commit=False)
                    reply.questionID = question
                    reply.owner = user
                    reply.save()
                    return redirect('question_detail', pk)

    return render(request, 'community/question_detail.html',
                  {'question': question, 'form': form, 'reply': reply, 'user': user, 'questionCheck': questionCheck,
                   'replyCheck': replyDict})


@login_required(login_url='login')
def question_create(request):
    profile = request.user
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.owner = profile
            question.save()
            return redirect('questions_list')
        else:
            context = {'form': form}
            return render(request, 'community/question_forms.html', context)

    context = {'form': form}
    return render(request, 'community/question_forms.html', context)


@login_required(login_url='login')
def question_update(request, pk):
    profile = request.user
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
    profile = request.user
    question = profile.question_set.get(id=pk)
    if request.method == "POST":
        question.delete()
        return redirect('questions_list')
    context = {'object': question}
    return render(request, 'community/question_delete.html', context)
