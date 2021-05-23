from django.shortcuts import render

posts = [
    {
        'author':'author1',
        'title':'Title1',
        'content':'Content1',
        'date_posted':'May 23, 2021'
    },
    {
        'author':'author2',
        'title':'Title2',
        'content':'Content2',
        'date_posted':'May 23, 2021'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)
