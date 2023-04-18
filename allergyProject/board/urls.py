from django.urls import path
from . import views as boardviews

app_name = 'board'

urlpatterns = [
    path('board/', boardviews.board, name='board'),
    path('bdetail/', boardviews.boarddetail, name='boarddetail'),
]

