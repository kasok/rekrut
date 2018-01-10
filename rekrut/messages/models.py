from django.db import models

# Create your models here.

class Message(models.Model):
    text = models.TextField(blank=True, null=True)
    recipient = models.CharField(max_length=256)
    read_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.recipient+" ===> : "+self.text
    def text_short(self):
        return self.text[:10]+" ..."