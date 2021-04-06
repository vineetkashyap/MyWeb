from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def team(request):
    return render(request,'team.html')


###############START INDUSTRIES##################
def agriculture(request):
        return render(request,'industries/agriculture.html')

def artificial(request):
        return render(request,'industries/artificial.html')

def construction(request):
        return render(request,'industries/construction.html')

def development(request):
        return render(request,'industries/development.html')

def ecommerce(request):
        return render(request,'industries/ecommerce.html')

def education(request):
        return render(request,'industries/education.html')

def fabrication(request):
        return render(request,'industries/fabrication.html')

def finance(request):
        return render(request,'industries/finance.html')

def goverment(request):
        return render(request,'industries/goverment.html')

def importandexport(request):
        return render(request,'industries/importandexport.html')

def itandites(request):
        return render(request,'industries/itandites.html')

def manufecturing(request):
        return render(request,'industries/manufecturing.html')

def mining(request):
        return render(request,'industries/mining.html')

def ngo(request):
        return render(request,'industries/ngo.html')

def privateindustries(request):
        return render(request,'industries/privateindustries.html')

def research(request):
        return render(request,'industries/research.html')

def retail(request):
        return render(request,'industries/retail.html')

def ruraldevelopment(request):
        return render(request,'industries/ruraldevelopment.html')

def solarandelectronics(request):
        return render(request,'industries/solarandelectronics.html')

def startupbusiness(request):
        return render(request,'industries/startupbussiness.html')

def survey(request):
        return render(request,'industries/survey.html')

def trainingandskill(request):
        return render(request,'industries/trainingandskill.html')

def transport(request):
        return render(request,'industries/transport.html')

def wastemanagement(request):
        return render(request,'industries/wastemanagement.html')

def waterresourses(request):
        return render(request,'industries/waterresourses.html')
###############-----END INDUSTRIES-----##################


###############-----START CAPABILITIES-----################
def  itdepartment(request):
    return render(request,'capabilities/itdepartment.html')

def  media(request):
    return render(request,'capabilities/media.html')

def  prandclientmanagement(request):
    return render(request,'capabilities/prandclientmanagement.html')

def  researchdepartment(request):
    return render(request,'capabilities/researchdepartment.html')
    
###############-----END CAPABILITIES-----##################
def contact(request):
        return render(request,'contact.html')