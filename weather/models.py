from django.db import models


# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="заглавие")
    content = models.TextField(blank=True, verbose_name="контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    update = models.DateTimeField(auto_now_add=True, verbose_name="дата обновления")
    photo = models.ImageField(upload_to="photos/%Y/%m/d/", verbose_name="фото")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
        ordering = ["created_at"]
