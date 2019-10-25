from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    '''
    Render the main page
    '''
    context = {'like':'Django 很棒'}
    return render(request, 'main/main.html', context)