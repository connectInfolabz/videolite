
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('index', index, name='index'),
    path('search', search, name='search'),
    path('video/<str:vid>', video, name='video'),
    path('channel/<str:cid>', channel, name='channel'),
    path('games', games, name='games'),
    path('songs', songs, name='songs'),
    path('movies', movies, name='movies'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('account', account, name='account'),
    path('registeruser', registeruser, name='registeruser'),
    path('verifyuser', verifyuser, name='verifyuser'),
    path('logout', logout, name='logout'),
    path('playlist/<str:cid>', playlist, name='playlist'),
    path('playlistvideos/<str:pid>', playlistvideos, name='playlist'),
    path("about/<str:cid>", about, name="about")
]
