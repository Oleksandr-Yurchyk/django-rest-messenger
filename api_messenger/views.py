from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api_messenger.models import Message
from api_messenger.regex_validators import is_email_valid, is_message_valid
from api_messenger.serializers import MessageSerializer


class MessageDetail(GenericAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get(self, request, pk):
        try:
            message = Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='There is no message by given id')
        serializer = MessageSerializer(message, context={'request': request})
        return Response(serializer.data)


class MessageList(GenericAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get(self, request, pk):
        messages = Message.objects.all()
        paginator = Paginator(messages.order_by('created_at'), 10)
        try:
            messages = paginator.page(pk)
        except EmptyPage:
            # If page is out of range, deliver first page of results.
            messages = paginator.page(1)

        serializer = MessageSerializer(messages, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        email = request.data.get('author_email')
        text = request.data.get('text')

        if not is_email_valid(email):
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Your email is not valid')

        if not is_message_valid(text):
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Your message text is not valid')

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
