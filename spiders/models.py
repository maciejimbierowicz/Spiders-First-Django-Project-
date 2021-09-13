from django.db import models

class Spider(models.Model):
    spider_image = models.ImageField(default='default.jpg', upload_to='spiders_pics')
    name = models.CharField(max_length=200)
    info = models.TextField(default='')
    difficulty = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
