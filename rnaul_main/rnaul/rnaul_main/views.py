from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def frontend(request): 
  return HttpResponse(render(request, 'vue_index.html'))
