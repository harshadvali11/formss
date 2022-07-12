
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def forms(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        return HttpResponse(username)
        #return HttpResponse('Form Submitted Success fully')
    return render(request,'forms.html')
def create_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        return HttpResponse('Topic is inserted Successfully')
    return render(request,'create_topic.html')


def create_webpage(request):
    if request.method=='POST':
        tn=request.POST['topic']
        na=request.POST['name']
        ul=request.POST['ul']
        t=Topic.objects.get_or_create(topic_name=tn)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=na,url=ul)[0]
        w.save()
        return HttpResponse('Webpage is inserterd')
    return render(request,'create_webpage.html')









