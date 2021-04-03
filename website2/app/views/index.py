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
    return render(request,'industries/agriculture.html')


def artificial(request):
    return render(request,'industries/artificial.html')

def education(request):
    return render(request,'industries/education.html')

def  ImportExprt(request):
    return render(request,'industries/import&export.html')

def mining(request):
    return render(request,'industries/mining.html')

def startup(request):
    return render(request,'industries/startup.html')

def training(request):
    return render(request,'industries/training.html')

def transport(request):
    return render(request,'industries/transport.html')

def it(request):
    return render(request,'industries/it.html')

def construction(request):
    return render(request,'industries/construction.html')

def fabrication(request):
    return render(request,'industries/fabrication.html')

def finance(request):
    return render(request,'industries/finance.html')

def goverment(request):
    return render(request,'industries/goverment.html')

def manufecturing(request):
    return render(request,'industries/manufecturing.html')

def research(request):
    return render(request,'industries/research.html')
    
def private(request):
    return render(request,'industries/privateIndustries.html')

def retail(request):
    return render(request,'industries/retail.html')

def ruraldevelopment(request):
    return render(request,'industries/ruraldevelopment.html')

def solarelectronics(request):
    return render(request,'industries/solarelectronics.html')

def survey(request):
    return render(request,'industries/survey.html')

def trust(request):
    return render(request,'industries/trust.html')

def wastemanagement(request):
    return render(request,'industries/WasteManagement.html')

def waterresources(request):
    return render(request,'industries/waterresources.html')

def ecommerse(request):
    return render(request,'industries/Ecommerse.html')


# ####################CAPABILITIES VIEW####################

def  itdepartment(request):
    return render(request,'capabilities/itdepartment.html')
def  media(request):
    return render(request,'capabilities/media.html')
def  pr(request):
    return render(request,'capabilities/pr.html')
def  research_dev(request):
    return render(request,'capabilities/research.html')
################Join Us###############
def  investor(request):
    return render(request,'joinus/investor.html')