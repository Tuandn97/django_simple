from datetime import date
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from chatbot.serializers import ConversationSerializer, SystemPromptSerializer
from chatbot.models import Conversation, SystemPrompt
from chatbot.chat_service.simple_chat_bot import get_message_from_chatbot



# Create your views here.
# Create CRUD for the Conversations model

class ListCreateConversation(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


list_create_conversation = ListCreateConversation.as_view()


class RetrieveUpdateDestroyConversation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


retrieve_update_destroy_conversation = RetrieveUpdateDestroyConversation.as_view()

class ListCreateSystemPrompt(generics.ListCreateAPIView):
    queryset = SystemPrompt.objects.all()
    serializer_class = SystemPromptSerializer

system_prompt_list_create = ListCreateSystemPrompt.as_view()

class RetrieveUpdateDestroySystemPrompt(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystemPrompt.objects.all()
    serializer_class = SystemPromptSerializer

system_prompt_retrieve_update_destroy = RetrieveUpdateDestroySystemPrompt.as_view()



class AnswerMessage(generics.ListCreateAPIView):
    serializer_class = []

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            conversation_id = data.get("conversation_id")
            message = data.get("message")
            output_message = get_message_from_chatbot(conversation_id, message)
            return Response({"AI message": output_message}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "failed"}, status=status.HTTP_400_BAD_REQUEST)


answer_message = AnswerMessage.as_view()
