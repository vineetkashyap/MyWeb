from django.shortcuts import render
from app.models import Blog,OurTeam
# Create your views here.
def  home(request):
    blogs=Blog.objects.all()
    teams=OurTeam.objects.all()
    return render(request,'index.html',{'blogs':blogs,'teams':teams})
def clock(request):
    return render(request,'clock.html')
def details(request):
    return render(request,'blog-details.html')
def signup(request):
    return render(request,'signup.html')
def team(request):
    teams=OurTeam.objects.all()
    return render(request,'team/team.html',{'teams':teams})
def contact(request):
    return render(request,'contact.html')
def agriculture(request):
    return render(request,'agriculture.html')

