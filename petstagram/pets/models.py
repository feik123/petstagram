from django.db import models
from django.utils.text import slugify


class Pets(models.Model):
    name = models.CharField(
        max_length=30,
    )
    pet_photo = models.URLField()
    date_of_birth = models.DateField(
        blank=True,
        unique=True,
    )

    slug = models.SlugField(unique=True, null=False, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        super().save(*args, **kwargs)


