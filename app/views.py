from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    QSTO=Topic.objects.all()
    d={'topic':QSTO}
    return render(request,'display_topic.html',d)

def display_Webpage(request):
    QSWO=Webpage.objects.all()
    d={'webpage':QSWO}
    return render(request,'display_Webpage.html',d)