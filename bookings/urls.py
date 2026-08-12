from django.urls import path
from . import views


app_name = "bookings"


urlpatterns = [

    path(
        "create/<int:event_id>/",
        views.booking_create,
        name="booking_form"
    ),

    path(
        "",
        views.booking_list,
        name="booking_list"
    ),

    path(
        "<int:pk>/",
        views.booking_detail,
        name="booking_detail"
    ),

    path(
        "<int:pk>/cancel/",
        views.booking_cancel,
        name="booking_cancel"
    ),
]