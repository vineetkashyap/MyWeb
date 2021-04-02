from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=500)
    posted_by=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    blog_image=models.ImageField(upload_to='blog')
    blog_date=models.DateField(auto_now=False, auto_now_add=False)

class OurTeam(models .Model):
    name=models.CharField(max_length=100)
    image= models.ImageField(upload_to="team")
    wing = models.CharField(max_length=90)
    description=models.TextField()
    facebook= models.URLField(max_length=200)
    linkedin= models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
 

