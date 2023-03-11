from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='index'),
    path('user-paste', views.UserPaste.as_view(), name='user-paste')
]
