from django.contrib import admin
from .models import City
from .models import News


# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id", "name")


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', "created_at", 'update', "is_published")
    search_fields = ("title", "content")
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    list_filter = ("is_published",)


admin.site.register(City, CityAdmin)
admin.site.register(News, NewsAdmin)
