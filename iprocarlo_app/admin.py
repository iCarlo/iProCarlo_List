from django.contrib import admin
from .models import Search, Filter


class FilterInLine(admin.StackedInline):
    model = Filter
    extra = 1


class SearchAdmin(admin.ModelAdmin):

    list_display = ('search_item', 'search_date',)
    
    fieldsets = [
        (None, {'fields': ['search_item']}),
        ('Date information', {'fields': ['search_date'], 'classes': ['collapse']}),
    ]

    inlines = [FilterInLine]

    list_filter = ('search_date',)


admin.site.register(Search, SearchAdmin)

admin.site.site_header = "iPro Carlo Adminstration"
