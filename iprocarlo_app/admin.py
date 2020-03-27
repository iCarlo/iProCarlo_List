from django.contrib import admin
from .models import Search, Filter
from django.utils import timezone


class FilterInLine(admin.TabularInline):
    model = Filter
    extra = 1
    max_num = 1


class SearchAdmin(admin.ModelAdmin):

    list_display = ('search_item', 'search_date', 'was_searched_recently', 'days_since_searched')
    list_filter = ('search_date',)
    search_fields = ('search_item',)
    list_per_page = 3

    actions = ('set_search_date_today',)

    fieldsets = [
        (None, {'fields': ['search_item']}),
        ('Date information', {'fields': ['search_date'], 'classes': ['collapse']}),
    ]
    inlines = [FilterInLine]

    def set_search_date_today(self, request, queryset):
        count = queryset.update(search_date=timezone.now())
        self.message_user(request, '{} Selected searches successfully set to searched now!'.format(count))

    set_search_date_today.short_description = "Mark selected searches as searched now"


admin.site.register(Search, SearchAdmin)
admin.site.site_header = "iPro Carlo Adminstration"
admin.site.site_title = "iPro Carlo Adminstration"
admin.site.index_title = "iPro Carlo Adminstration"
