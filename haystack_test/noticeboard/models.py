from django.db import models

# Create your models here.

class Notice(models.Model):
    ORGANIZATION_CHOICES = (
        ('KIN', 'KIN'),
        ('SSA', 'SUST Science Arena'),
        ('DIK', 'Dik Theater'),
    )
    title = models.CharField(max_length=150)
    body = models.TextField(blank=True)
    pubdate = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    organization = models.CharField(max_length=3, choices=ORGANIZATION_CHOICES)

    class Meta:
        verbose_name_plural = "Notice Board"
        ordering = ["-pubdate"]

    def __unicode__(self):
        return self.title[:50]

