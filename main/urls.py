from django.urls import path

from main.views import index, retrieve_or_delete_content, clear_all_content

urlpatterns = [
    path('', index),
    path('<str:pk>/contents/clear', clear_all_content),
    path('<str:pk>', retrieve_or_delete_content, name='retrieve_or_delete_content'),
]