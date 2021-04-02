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
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
