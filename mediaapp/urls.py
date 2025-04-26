# multimedia_project/urls.py

from django.contrib import admin
from django.urls import path, include
from mediaapp.views import run_migrations  # ✅ import run_migrations
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Main app urls
    path('', include('mediaapp.urls')),  # ✅ Now, handle upload/, edit/, delete/ from mediaapp.urls
    
    # Special migration run
    path('runnow/', run_migrations),  # ✅ special route
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
