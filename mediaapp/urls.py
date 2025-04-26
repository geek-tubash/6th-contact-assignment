# multimedia_project/urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mediaapp.views import upload_media, media_list, edit_media, delete_media, run_migrations  # ✅

urlpatterns = [
    path('upload/', upload_media, name='upload_media'),
    path('', media_list, name='media_list'),
    path('edit/<int:pk>/', edit_media, name='edit_media'),
    path('delete/<int:pk>/', delete_media, name='delete_media'),
    path('runnow/', run_migrations),  # ✅ for migrations
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
