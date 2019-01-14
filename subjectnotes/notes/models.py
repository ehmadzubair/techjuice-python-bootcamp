from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)


class Note(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()

    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
