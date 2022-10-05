from . import views
from django.urls import path


urlpatterns = [
        path('', views.home, name=''),
        path('home', views.home, name='home'),
        path('log', views.LoginPage, name='login'),
        path('logout', views.logoutUser, name='logout'),
        path('register', views.registerUser, name='register'),
        path('mouse', views.mouse, name='mouse'),
        path('micro', views.micro, name='micro'),
        path('headphoneRoom', views.headphoneRoom, name='headphone'),
        path('headphone', views.headphone, name='headphone'),
        path('microRoom', views.microRoom, name='micro'),
        path('mouseRoom', views.mouseRoom, name='mouse'),
        path('successRoom', views.successRoom, name='successRoom'),
               


        ]

