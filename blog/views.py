from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_list(request):
    title = "Welcome to the Django Blog"
    return render(request, 'blog/post_list.html', {'title': title})
