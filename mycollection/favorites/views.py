from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from .models import FavoriteThing
from .forms import FavoriteThingForm, SearchForm, SignUpForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'favorites/login.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'favorites/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    form = SearchForm(request.GET or None)
    favorites = FavoriteThing.objects.filter(user=request.user)
    
    if form.is_valid():
        if form.cleaned_data['query']:
            favorites = favorites.filter(name__icontains=form.cleaned_data['query'])
        if form.cleaned_data['category']:
            favorites = favorites.filter(category=form.cleaned_data['category'])
        if form.cleaned_data['min_rating']:
            favorites = favorites.filter(rating__gte=form.cleaned_data['min_rating'])
    
    favorites = favorites.order_by('category', '-rating', 'name')
    
    categories = {
        'SONG': favorites.filter(category='SONG'),
        'GAME': favorites.filter(category='GAME'),
        'MOVIE': favorites.filter(category='MOVIE'),
    }
    
    return render(request, 'favorites/dashboard.html', {
        'categories': categories,
        'search_form': form,
        'has_results': favorites.exists()
    })

@login_required
def add_favorite(request):
    if request.method == 'POST':
        form = FavoriteThingForm(request.POST, request.FILES)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.user = request.user
            favorite.save()
            return redirect('dashboard')
    else:
        form = FavoriteThingForm()
    return render(request, 'favorites/favorite_form.html', {'form': form, 'title': 'Add New Favorite'})

@login_required
def edit_favorite(request, pk):
    favorite = get_object_or_404(FavoriteThing, pk=pk, user=request.user)
    if request.method == 'POST':
        form = FavoriteThingForm(request.POST, request.FILES, instance=favorite)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FavoriteThingForm(instance=favorite)
    return render(request, 'favorites/favorite_form.html', {'form': form, 'title': 'Edit Favorite'})

@login_required
def delete_favorite(request, pk):
    favorite = get_object_or_404(FavoriteThing, pk=pk, user=request.user)
    if request.method == 'POST':
        favorite.delete()
        return redirect('dashboard')
    return render(request, 'favorites/confirm_delete.html', {'favorite': favorite})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'favorites/signup.html', {'form': form})