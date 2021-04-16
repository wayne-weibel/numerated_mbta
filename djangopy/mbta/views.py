"""mbta views"""
from django.shortcuts import render

# Create your views here.

def index(request):
    """index page for mbta app"""
    context = {"count": int(request.POST.get('count', -1)) + 1}


    return render(request, 'mbta/index.html', context)
