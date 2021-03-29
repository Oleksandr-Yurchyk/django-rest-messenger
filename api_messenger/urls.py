from django.urls import path
from . import views

urlpatterns = [
    path('list/<int:pk>', views.MessageList.as_view()),
    path('single/<int:pk>', views.MessageDetail.as_view()),
]
