from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
def emailsend(request):
    name1= request.POST['Fname']
    name2 = request.POST['Lname']
    email = request.POST['email']
    subject = request.POST['sub']
    message = request.POST['message']  
    print("=========================>>>>>>>>>>>",name1)
    print("=========================>>>>>>>>>>>",name2)
    print("=========================>>>>>>>>>>>",email)
    print("=========================>>>>>>>>>>>",subject)
    print("=========================>>>>>>>>>>>",message)
    # context={'name':name,'email':email,'subject':subject,'message':message}
    template = render_to_string('email.html')
    email = EmailMessage(
        subject,
        template,
        email,
        [settings.EMAIL_HOST_USER],
    )
    email.fail_silently=False
    email.send()
    return redirect("index")    