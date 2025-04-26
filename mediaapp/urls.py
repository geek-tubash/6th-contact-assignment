from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

# --- Add this import at the top ---
import os
from django.core.management import call_command

# --- Then, only run migrate if on server (optional but better) ---
if os.environ.get('IS_SERVER') == 'true':
    call_command('migrate')

urlpatterns = [
    path('upload/', views.upload_media, name='upload_media'),
    path('', views.media_list, name='media_list'),
    path('edit/<int:pk>/', views.edit_media, name='edit_media'),
    path('delete/<int:pk>/', views.delete_media, name='delete_media'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
