from django.urls import path
from app.views import index,email
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index.home,name='index'),
    path('clock/',index.clock,name='clock'),
    path('details/',index.details,name="details"),
    path('signup/',index.signup,name="signup"),
    path('email/',email.emailsend,name="email"),
    path('team/',index.team,name="team"),
    path('contact/',index.contact,name="contact"),
    path('agri/',index.agriculture,name="agri"),
    path('artificial/',index.artificial,name="artificial"),
    path('education/',index.education,name="education"),
    path('ImportExprt/',index.ImportExprt,name="ImportExprt"),
    path('mining/',index.mining,name="mining"),
    path('startup/',index.startup,name="startup"),
    path('training/',index.training,name="training"),
    path('transport/',index.transport,name="transport"),
    path('it/',index.it,name="it"),
    path('construction/',index.construction,name="construction"),
    path('fabrication/',index.fabrication,name="fabrication"),
    path('finance/',index.finance,name="finance"),
    path('goverment/',index.goverment,name="goverment"),
    path('manufecturing/',index.manufecturing,name="manufecturing"),
    path('research/',index.research,name="research"),
    path('private/',index.private,name="private"),
    path('retail/',index.retail,name="retail"),
    path('ruraldevelopment/',index.ruraldevelopment,name="ruraldevelopment"),
    path('solarelectronics/',index.solarelectronics,name="solarelectronics"),
    path('survey/',index.survey,name="survey"),
    path('trust/',index.trust,name="trust"),
    path('wastemanagement/',index.wastemanagement,name="wastemanagement"),
    path('waterresources/',index.waterresources,name="waterresources"),
    path('ecommerse/',index.ecommerse,name="ecommerse"),
###############capabilities
    path('itdepartment/',index.itdepartment,name="itdepartment"),
    path('media/',index.media,name="media"),
    path('pr/',index.pr,name="pr"),
    path('research_dev/',index.research_dev,name="research_dev"),
    path('investor/',index.investor,name="investor"),
    
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
