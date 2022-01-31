from django.urls import path, re_path

from . import views

urlpatterns = [
    # Get the Greeks for a Contract
    re_path(r'^.*\.html', views.pages, name='pages'),
    path('', views.index, name='home'),
    path('leaderboard', views.leaderboards, name='leaderboard.html'),
    path('perfectbracket', views.perfectbracket, name='perfectbracket.html'),
    path('update', views.update, name='update.html'),
    path('bracket/<id>/', views.bracket, name='bracket.html'),

]
