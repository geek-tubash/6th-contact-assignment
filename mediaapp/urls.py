from django.urls import path
from .views import upload_media, media_list, edit_media, delete_media, migrate_now

urlpatterns = [
    path('upload/', upload_media, name='upload_media'),
    path('', media_list, name='media_list'),
    path('edit/<int:pk>/', edit_media, name='edit_media'),
    path('delete/<int:pk>/', delete_media, name='delete_media'),
    path('migrate-now/', migrate_now, name='migrate_now'),  # ✅ Added migrate_now
]
