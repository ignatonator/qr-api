from django.db import models

# Create your models here.
class QrCode(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=4000)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by = "created"
        ordering=['created']
        verbose_name="QR Code"
        verbose_name_plural="QR Codes"
    def __str__(self):
        return self.title