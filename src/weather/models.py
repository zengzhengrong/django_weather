from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=20)
    # temperature = models.IntegerField(verbose_name='℃')
    is_cn = models.BooleanField(default=False,verbose_name='China weather')
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_time']
        verbose_name_plural='weathers'
    def __str__(self):
        return self.name

