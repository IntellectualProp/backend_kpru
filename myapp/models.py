from django.db import models

class WebsiteSetting(models.Model):
    tag = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    image_binary = models.BinaryField(blank=True, null=True)
    image_file_name = models.CharField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.tag
