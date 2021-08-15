from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kumar(request):
    return render(request,'kumar.html')
