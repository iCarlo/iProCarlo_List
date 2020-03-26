from django.db import models

# Create your models here.


class Search(models.Model):
    search_item = models.CharField(max_length=200)
    search_date = models.DateTimeField('date published')

    def __str__(self):
        return '{}'.format(self.search_item)

    class Meta:
        verbose_name_plural = 'Searches'


class Filter(models.Model):
    searched = models.ForeignKey(Search, on_delete=models.CASCADE)
    filter_text = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.filter_text)

    class Meta:
        verbose_name_plural = 'Filters'
