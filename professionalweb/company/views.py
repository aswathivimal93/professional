from django.shortcuts import render
from .models import services,members
# Create your views here.
def home(request):
    result=services.objects.all()
    memberresults=members.objects.all()
    return render(request,'index.html',{'result':result,'memberresults':memberresults})
