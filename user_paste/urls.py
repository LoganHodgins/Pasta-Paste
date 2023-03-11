from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserPaste.as_view(), name='user-paste')
]
