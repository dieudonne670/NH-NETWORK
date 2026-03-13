# feedback/models.py
from django.db import models




# Base model for provider-specific feedback
class BaseFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # No DB table created

    def __str__(self):
        return f"{self.name} - {self.date_submitted.strftime('%Y-%m-%d %H:%M')}"


# MTN Feedback
class MTNFeedback(BaseFeedback):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)  # Mbps
    rating = models.IntegerField(default=0)

# Orange Feedback   
class OrangeFeedback(BaseFeedback):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)  # Mbps
    rating = models.IntegerField(default=0)


# Camtel Feedback
class CamtelFeedback(BaseFeedback):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)  # Mbps
    rating = models.IntegerField(default=0)


# Nexttel Feedback
class NexttelFeedback(BaseFeedback):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)  # Mbps
    rating = models.IntegerField(default=0)
