from django.db import models
from django.shortcuts import reverse

class TodoItem(models.Model):
    name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("todoclass:detail", kwargs={"pk": self.id})

    def get_absolute_url2(self):
        return reverse("todofunc:detail", kwargs={"id": self.id})