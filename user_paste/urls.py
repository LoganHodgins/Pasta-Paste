from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='index'),
    path('user-paste', views.UserPaste.as_view(), name='user-paste'),
    path('paste/<slug:slug>', views.Paste.as_view(), name='paste-page'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('view-pastes', views.ViewPaste.as_view(), name='view-pastes')
]
