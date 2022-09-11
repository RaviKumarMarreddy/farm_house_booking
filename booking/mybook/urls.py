from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('signout/', views.signout),
    path('restro/',views.restro),
    path('tents/',views.tents),
]
