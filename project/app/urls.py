from django.urls import path
from .views import RegisterUserView , UserLoginView , VideoUploadView


urlpatterns = [
    path('user/login/' , UserLoginView.as_view() , name='user-login'),
    path('user/register/' , RegisterUserView.as_view() , name='user-register'),
     path('upload/', VideoUploadView.as_view(), name='video-upload'),

]