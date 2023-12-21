from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
# Create your views here.
def display_topic(request):
    QSTO=Topic.objects.all()
    QSTO=Topic.objects.all().order_by('topic_name')
    QSTO=Topic.objects.all().order_by('-topic_name')
    QSTO=Topic.objects.all().order_by(Length('topic_name'))
    QSTO=Topic.objects.all().order_by(Length('topic_name').desc())

    d={'topic':QSTO}
    return render(request,'display_topic.html',d)

    


def display_Webpage(request):
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
    QSWO=Webpage.objects.filter(topic_name='cricket')
    QSWO=Webpage.objects.filter(pk__lte=5)
    QSWO=Webpage.objects.filter(pk__gte=5)
    QSWO=Webpage.objects.filter(pk__lt=5)
    QSWO=Webpage.objects.filter(pk__gt=5)
    QSWO=Webpage.objects.filter(name__startswith='r')
    QSWO=Webpage.objects.filter(name__endswith='i')
    
    d={'webpage':QSWO}
    return render(request,'display_Webpage.html',d)

def display_access(request):
    DARO=AccessRecord.objects.all()
    d={'access':DARO}
    return render(request,'display_access.html',d)

    

def insert_topic(request):
    tn=input('enter topic name :  ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('topic is created.....')

def insert_webpage(request):
    tn=input('enter topic name ')
    n=input('enter name ')
    u=input('enter url ')
    e=input('enter email ')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=tn,name=n,url=u,email=e)[0]
    NWO.save()
    return HttpResponse('webpage is created')

def insert_access(request):
    pk=int(input('enter pk value for webpage'))
    a=input('enter author')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return HttpResponse('access record is created')
