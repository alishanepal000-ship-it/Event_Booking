from django.contrib import admin
from .models import Event, Category, Organizer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
    )
    search_fields = (
        "name",
        "email",
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "date",
        "start_time",
        "location",
        "price",
        "capacity",
        "organizer",
        "category",
    )
    search_fields = ("title", "location")
    list_filter = ("date", "category")