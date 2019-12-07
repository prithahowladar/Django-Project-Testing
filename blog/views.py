from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author':'Pritha',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'Today',

    },
{
        'author':'Pritha Again',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'Yesterday',

    }
]
def home(request):
    context ={ 'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

