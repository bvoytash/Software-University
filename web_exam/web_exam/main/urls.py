from django.urls import path

from web_exam.main.views import home_page, create_profile, dashboard, create_game, details_game, edit_game, delete_game, \
    profile_details, edit_profile, profile_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path('dashboard/', dashboard, name='dashboard'),

    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', details_game, name='game details'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),

    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', edit_profile, name='profile edit'),
    path('profile/delete/', profile_delete, name='delete profile'),
    path('profile/create', create_profile, name='create profile'),
]