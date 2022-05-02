from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    delete_at = models.DateTimeField(null=True, blank=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True