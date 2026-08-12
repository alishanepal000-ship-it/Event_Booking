from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from events.models import Event

from .forms import BookingForm
from .models import Booking


@login_required
def booking_create(request, event_id):

    event = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":

        form = BookingForm(
            request.POST,
            event=event
        )

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user
            booking.event = event
            booking.status = "confirmed"

            booking.save()

            messages.success(
                request,
                "Your booking has been confirmed!"
            )

            return redirect(
                "bookings:booking_detail",
                pk=booking.pk
            )

    else:

        form = BookingForm(event=event)

    return render(
        request,
        "bookings/booking_form.html",
        {
            "form": form,
            "event": event,
        }
    )


@login_required
def booking_list(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).select_related("event")

    return render(
        request,
        "bookings/booking_list.html",
        {
            "bookings": bookings
        }
    )


@login_required
def booking_detail(request, pk):

    booking = get_object_or_404(
        Booking.objects.select_related("event", "user"),
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "bookings/booking_detail.html",
        {
            "booking": booking
        }
    )


@login_required
def booking_cancel(request, pk):

    booking = get_object_or_404(
        Booking,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        booking.status = "cancelled"
        booking.save()

        messages.success(
            request,
            "Your booking has been cancelled."
        )

        return redirect(
            "bookings:booking_list"
        )

    return render(
        request,
        "bookings/booking_confirm_cancel.html",
        {
            "booking": booking
        }
    )