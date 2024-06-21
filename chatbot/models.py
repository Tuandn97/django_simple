from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Conversation(models.Model):
   id = models.AutoField(primary_key=True)
   character = models.CharField(max_length=100)
   gpt_model = models.CharField(max_length=100)
   chat_history = ArrayField(models.JSONField(), default=list) #{"role": "user", "content": "Hello! How are you?"}
   meta_data = models.JSONField(default=dict, null=True, blank=True)

   def __str__(self):
      return f"{self.id}"

class SystemPrompt(models.Model):
   id = models.AutoField(primary_key=True)
   character = models.CharField(max_length=100)
   prompt = models.CharField(max_length=100, unique=True)

   def __str__(self):
      return self.character