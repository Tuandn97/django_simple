"""
URL configuration for django_chatbot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from chatbot.views import list_create_conversation, retrieve_update_destroy_conversation, answer_message, system_prompt_list_create, system_prompt_retrieve_update_destroy

urlpatterns = [
    path("admin/", admin.site.urls),
    path("conversations/", list_create_conversation, name="list_create_conversation"),
    path("conversations/<int:pk>/", retrieve_update_destroy_conversation, name="retrieve_update_destroy_conversation"),
    path("system-prompts/", system_prompt_list_create, name="system_prompt_list_create"),
    path("system-prompts/<int:pk>/", system_prompt_retrieve_update_destroy, name="system_prompt_retrieve_update_destroy"),
    path("answer/", answer_message, name="answer_message"),
]
