from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm, StudentRegistrationForm
from .models import Student


def home(request):
    return render(request, 'home.html')



def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return render(request, 'home.html', {'data': data})
    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})

