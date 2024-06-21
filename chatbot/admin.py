from django.contrib import admin

# Register your models he
from chatbot.models import Conversation, SystemPrompt

admin.site.register(Conversation)
admin.site.register(SystemPrompt)