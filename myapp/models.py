from django.db import models


class WebsiteSetting(models.Model):
    tag = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    image_binary = models.BinaryField(blank=True, null=True)
    image_file_name = models.CharField(
        max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.tag


class IpKnowledge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_binary = models.BinaryField(blank=True, null=True)
    image_file_name = models.CharField(
        max_length=255, unique=True, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BulkImageUpload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)


class BulkImage(models.Model):
    upload = models.ForeignKey(
        BulkImageUpload, on_delete=models.CASCADE, related_name='images')
    image_binary = models.BinaryField()
    image_file_name = models.CharField(max_length=255)

    def __str__(self):
        return self.image_file_name
