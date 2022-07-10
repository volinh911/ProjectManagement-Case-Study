from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage/homepage.html')


def testButton(request):
    return render(request, 'homepage/test.html')


answerDic = {'context1': 10, 'context2': 20, 'context3': 5}
dic2 = dict(sorted(answerDic.items(), key=lambda x: x[1]))


def testVote(request):
    context = 10
    print(dic2)
    if request.method == "POST":
        if request.POST.get('buttonDown'):
            context -= 1
        elif request.POST.get('buttonUp'):
            context += 1
        print(request.POST.get('button', 'default-if-not-present'))

    return render(request, 'homepage/test.html', {'context': dic2})
