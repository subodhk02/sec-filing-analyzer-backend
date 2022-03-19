from django.db import models

class ErrorLogging(models.Model):
    context = models.TextField(blank=True, null=True)
    exception = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)