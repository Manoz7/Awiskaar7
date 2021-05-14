from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length = 255, blank=True)
    email = models.EmailField(max_length=50, blank= True)
    subject = models.CharField(max_length = 255, blank=True)
    message = models.CharField(max_length = 255, blank=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name