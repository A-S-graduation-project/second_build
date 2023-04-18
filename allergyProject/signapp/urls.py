from django.urls import path
from . import views as signviews

app_name = 'signapp'

urlpatterns = [
    path('login/', signviews.Mypage, name='login'),
    path('mypage/', signviews.Login, name='mypage'),
    # path('/', signviews.Logout , name='logout'),
]
