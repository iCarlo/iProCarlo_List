import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'Customers'


class Filter(models.Model):
    filter_text = models.CharField(max_length=200, null=True)
    filter_code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '{}'.format(self.filter_text)

    class Meta:
        verbose_name_plural = 'Filters'


class Search(models.Model):
    search_item = models.CharField(max_length=200)
    search_date = models.DateTimeField(auto_now_add=True, null=True)
    filter = models.ForeignKey(Filter, null=True, on_delete=models.SET_NULL)

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


class History(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    search = models.ForeignKey(Search, null=True, on_delete=models.SET_NULL)
    filter = models.ForeignKey(Filter, null=True, on_delete=models.SET_NULL)
    history_date = models.DateTimeField(auto_now_add=True, null=True)

    def was_history_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.history_date <= now
    was_history_recently.admin_order_field = 'history_date'
    was_history_recently.boolean = True
    was_history_recently.short_description = 'History recently?'

    def __str__(self):
        return '{}'.format(self.customer)

    class Meta:
        verbose_name_plural = 'Histories'
