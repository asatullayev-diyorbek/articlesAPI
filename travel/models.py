from django.db import models


class Hotel(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Narx ($)")
    image = models.ImageField(upload_to='hotel/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Mehmonxona'
        verbose_name_plural = 'Mehmonxonalar'

    def get_image(self):
        if self.image:
            return self.image.url
        return '/media/default.jpg'


class Class(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Narx ($)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Klass'
        verbose_name_plural = 'Klasslar'


class Travel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    period_amount = models.IntegerField(help_text="Muddatning miqdori (1, 4, 5 ...)")
    period_unit = models.CharField(max_length=30, help_text="Muddatning birligi (kun, hafta, oy ...)")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Narx ($)")
    travel_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tur'
        verbose_name_plural = 'Turlar'
