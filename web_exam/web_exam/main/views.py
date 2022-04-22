from django.shortcuts import render, redirect

from web_exam.main.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm
from web_exam.main.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


""" HOME PAGE """


def home_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


"""  PROFILE """


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
    return render(request, 'create-profile.html', context)


def dashboard(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'dashboard.html', context)


def profile_details(request):
    profile = Profile.objects.all().first()
    games_count = len(Game.objects.all())
    all_ratings = 0
    games = Game.objects.all()

    for g in games:
        all_ratings += g.rating

    if games_count:
        average_rating = all_ratings / games_count
    else:
        average_rating = float(0)
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.all().first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.all().first()
    games = Game.objects.all()
    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home page')

    context = {
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)


""" THE OBJECT """


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = CreateGameForm()
    context = {
        'form': form
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'form': form,
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        game.delete()
        return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'delete-game.html', context)
