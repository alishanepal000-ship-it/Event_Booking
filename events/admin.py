from django.contrib import admin
from .models import Event, Booking

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'capacity', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('date',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'booked_at')
    search_fields = ('user__username', 'event__title')
    list_filter = ('booked_at',)