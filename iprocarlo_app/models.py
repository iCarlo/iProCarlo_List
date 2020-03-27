import datetime
from django.db import models
from django.utils import timezone


class Search(models.Model):
    search_item = models.CharField(max_length=200)
    search_date = models.DateTimeField('date searched')

    def was_searched_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.search_date <= now
    was_searched_recently.admin_order_field = 'search_date'
    was_searched_recently.boolean = True
    was_searched_recently.short_description = 'Searched recently?'

    def days_since_searched(self):
        diff = timezone.now() - self.search_date
        return diff.days
    days_since_searched.short_description = 'No. days since searched'

    def __str__(self):
        return '{}'.format(self.search_item)

    class Meta:
        verbose_name_plural = 'Searches'


class Filter(models.Model):
    searched = models.ForeignKey(Search, null=True, on_delete=models.CASCADE)
    filter_text = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.filter_text)

    class Meta:
        verbose_name_plural = 'Filters'
