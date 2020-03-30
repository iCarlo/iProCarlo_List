from django.contrib import admin
from .models import Search, Filter, Customer, History
from django.utils import timezone


admin.site.register(Search)
admin.site.register(Customer)
admin.site.register(Filter)
admin.site.register(History)
admin.site.site_header = "iPro Carlo Adminstration"
admin.site.site_title = "iPro Carlo Adminstration"
admin.site.index_title = "iPro Carlo Adminstration"
