from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from examWeb.web.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from examWeb.web.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()
    if profile:
        context = {
            'albums': albums,
            'profile': profile,
        }
        return render(request, 'home-with-profile.html', context)
    return redirect('create profile')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = CreateProfileForm()
    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = CreateAlbumForm()
    context = {
        'form': form
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = Profile.objects.all().first()
    albums_count = len(Album.objects.all())
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = Profile.objects.all().first()
    albums = Album.objects.all()
    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('home page')

    context = {
        'profile': profile,
    }
    return render(request, 'profile-delete.html', context)

