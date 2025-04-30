from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from favorites import views

urlpatterns = [
    # Authentication URLs
    path('', views.login_view, name='root'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard and favorite management URLs
    path('dashboard/', login_required(views.dashboard), name='dashboard'),
    path('dashboard/add/', login_required(views.add_favorite), name='add_favorite'),
    path('dashboard/edit/<int:pk>/', login_required(views.edit_favorite), name='edit_favorite'),
    path('dashboard/delete/<int:pk>/', login_required(views.delete_favorite), name='delete_favorite'),
    
    # Admin URL
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)