from django.db import models

# Create your models here.


class Search(models.Model):
    search_item = models.CharField(max_length=200)
    search_date = models.DateTimeField('date published')

    def __str__(self):
        return '{}'.format(self.search_item)

    class Meta:
        verbose_name_plural = 'Searches'
