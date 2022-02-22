from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    # many-to-many relationship with Link referenced on Link class.
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"tag: self.tag_name"})


class Link(models.Model):
    link_name = models.CharField(max_length=255)
    link_path = models.URLField()
    image = models.URLField()
    notes = models.TextField()
    tags = models.ManyToManyField(Tag)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.link_name

    def get_absolute_url(self):
        return reverse("link_detail", kwargs={"title: self.title"})