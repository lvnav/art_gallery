from django.db import models
from django.utils.timezone import now

class Author(models.Model):
    main_picture_url = models.CharField(max_length=500)
    biography = models.CharField(max_length=1000)
    created_at = models.DateField(default=now, null=False)
    updated_at = models.DateField(default=now, null=False)

class Artwork(models.Model):
    url = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    publication_date = models.DateField()
    created_at = models.DateField(default=now, null=False)
    updated_at = models.DateField(default=now, null=False)

