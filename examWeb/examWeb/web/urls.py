from django.urls import path

from examWeb.web.views import home_page, add_album, details_album, edit_album, delete_album, profile_details, \
    create_profile, profile_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', details_album, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),

    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', profile_delete, name='delete profile'),
    path('profile/create', create_profile, name='create profile'),
]
