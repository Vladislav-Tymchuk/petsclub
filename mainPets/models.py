from django.db import models

class Banner(models.Model):
    bannerImage = models.ImageField(upload_to="images")
    bannerDescription = models.TextField(max_length=254)

    def __str__(self):
        return self.bannerDescription