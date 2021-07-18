from django.urls import path

from main.views import index, retrieve_or_delete_content

urlpatterns = [
    path('', index),
    path('<str:pk>', retrieve_or_delete_content, name='retrieve_or_delete_content'),
]