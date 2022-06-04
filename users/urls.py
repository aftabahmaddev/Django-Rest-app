from django.urls import path
from .views import register, user, hello, login
urlpatterns = [
    path('', hello),
    path('user/', user),
    path('register/', register),
    path('login/', login)

]
