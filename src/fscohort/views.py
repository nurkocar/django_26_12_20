from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

def home_view(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    form = StudentForm()
    my_context = {
        'title' : '<b>clarusway</b>',
        'dict1' : {'django': 'best framework'},
        'my_list': [1,2,3,4,5],
        'cat' : 'mavis',
        'studentForm' : form
    }
    
    return render(request, 'fscohort/home.html', my_context)

def about_view(request):
    return HttpResponse("<h1>Hi, this is about page.</h1>")