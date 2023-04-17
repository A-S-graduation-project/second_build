from django.urls import path
from . import views as signviews

app_name = 'signapp'

urlpatterns = [
    path('login/', signviews.Login, name='login'),
    # path('/', signviews.Logout , name='logout'),
]
