from django.core.paginator import Paginator, EmptyPage
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api_messenger.models import Message
from api_messenger.serializers import MessageSerializer


class MessageDetail(GenericAPIView):
    """Class for view a specific message"""
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get(self, request, pk):
        try:
            message = self.queryset.get(pk=pk)
        except Message.DoesNotExist:
            # Changed Response to JsonResponse
            return JsonResponse(
                status=400,
                data={"error_message": 'There is no message by given id'}
            )

        serializer = MessageSerializer(message, context={'request': request})
        return Response(serializer.data)


class MessageList(GenericAPIView):
    """Class for view a list with messages with pagination by 10"""

    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def get(self, request, pk):
        messages = self.queryset
        paginator = Paginator(messages.order_by('created_at'), 10)
        try:
            messages = paginator.page(pk)
        except EmptyPage:
            # Changed the display of first page to the last
            messages = paginator.page(paginator.num_pages)

        serializer = MessageSerializer(messages, context={'request': request}, many=True)
        return Response(serializer.data)


class CreateMessage(GenericAPIView):
    """Class for create a message"""

    serializer_class = MessageSerializer

    # No more id is needed to create a message
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

        return Response(serializer.errors, status=400)
