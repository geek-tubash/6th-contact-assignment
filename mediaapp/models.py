from django.db import models

class MediaFile(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('file', 'Other'),
    ]

    title = models.CharField(max_length=255)  # Ensure the title field is present
    file = models.FileField(upload_to='mediafiles/')  # Path where media files are stored
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)  # Choices for media type
    tags = models.CharField(max_length=255, blank=True)  # Optional tags for categorizing
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp when uploaded

    def __str__(self):
        return self.title  # Represents media file by title
