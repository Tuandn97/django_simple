from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Conversation(models.Model):
   id = models.AutoField(primary_key=True)
   chat_history = ArrayField(models.CharField(), default=list)
   gpt_model = models.CharField(max_length=100)
   character = models.CharField(max_length=100)