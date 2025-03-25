from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    image_binary = models.BinaryField(blank=True, null=True)  # Save image as binary data
    image_file_name = models.CharField(max_length=255, blank=True, null=True)  # Store image file name

    def __str__(self):
        return self.title
