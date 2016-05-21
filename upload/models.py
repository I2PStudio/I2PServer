from django.db import models


class File(models.Model):
    url = models.URLField('链接')
    create_at = models.DateTimeField(auto_created=True)
    mime_type = models.CharField(max_length=32)
    hash = models.CharField(max_length=255, null=True)
