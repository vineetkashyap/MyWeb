
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('team/',views.team,name='team'),
    ##########INDUTRIES URLS################
    path('agriculture/',views.agriculture,name='agriculture'),
    path('artificial/',views.artificial,name='artificial'),
    path('construction/',views.construction,name='construction'),
    path('development/',views.development,name='development'),
    path('ecommerce/',views.ecommerce,name='ecommerce'),        
    path('education/',views.education,name='education'),        
    path('fabrication/',views.fabrication,name='fabrication'),        
    path('finance/',views.finance,name='finance'),        
    path('goverment/',views.goverment,name='goverment'),        
    path('importandexport/',views.importandexport,name='importandexport'),        
    path('itandites/',views.itandites,name='itandites'),        
    path('manufecturing/',views.manufecturing,name='manufecturing'),        
    path('mining/',views.mining,name='mining'),        
    path('ngo/',views.ngo,name='ngo'),        
    path('privateindustries/',views.privateindustries,name='privateindustries'),        
    path('research/',views.research,name='research'),        
    path('retail/',views.retail,name='retail'),        
    path('ruraldevelopment/',views.ruraldevelopment,name='ruraldevelopment'),        
    path('solarandelectronics/',views.solarandelectronics,name='solarandelectronics'),        
    path('startupbusiness/',views.startupbusiness,name='startupbusiness'),        
    path('survey/',views.survey,name='survey'),        
    path('trainingandskill/',views.trainingandskill,name='trainingandskill'),        
    path('transport/',views.transport,name='transport'),        
    path('wastemanagement/',views.wastemanagement,name='wastemanagement'),        
    path('waterresourses/',views.waterresourses,name='waterresourses'),        

    ##########CAPABILITIES URLS#############
    path('itdepartment/',views.itdepartment,name="itdepartment"),
    path('media/',views.media,name="media"),
    path('prandclientmanagement/',views.prandclientmanagement,name="prandclientmanagement"),
    path('researchdepartment/',views.researchdepartment,name="researchdepartment"),
###############contact#########################.
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('whatwedo/',views.whatwedo,name="whatwedo"),
    path('whoweare/',views.whoweare,name="whoweare"),
    path('whatwebelieve/',views.whatwebelieve,name="whatwebelieve"),

]
