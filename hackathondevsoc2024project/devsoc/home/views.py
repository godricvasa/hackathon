from django.shortcuts import render, redirect
from .forms import QuestionForm


def home(request):
    return render(request, "homepage.html")


def query(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question_list')  # Redirect to a page displaying the list of questions
    else:
        
        form = QuestionForm()
    return render(request, 'query.html', {'form': form})


def answer(request):
    pass




