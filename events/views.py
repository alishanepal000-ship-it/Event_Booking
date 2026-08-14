from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Case, When, IntegerField
from django.core.exceptions import PermissionDenied
from .models import Event, Category
from .forms import EventForm


def home(request):
    events = Event.objects.all().order_by("date")
    return render(request,"events/home.html",{"events": events,},)

def event_list(request):
    categories = Category.objects.all().order_by(
        Case(
            When(name="Other", then=1),
            default=0,
            output_field=IntegerField(),
        ),
        "name",
    )

    category_id = request.GET.get("category")

    if category_id:
        events = Event.objects.filter(
            category_id=category_id
        ).order_by("date")
    else:
        events = Event.objects.all().order_by("date")

    return render(
        request,
        "events/event_list.html",
        {
            "events": events,
            "categories": categories,
            "selected_category": category_id,
        },
    )


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)

    return render(
        request,
        "events/event_detail.html",
        {"event": event},
    )


def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save()

            return redirect(
                "events:event_detail",
                pk=event.pk
            )
    else:
        form = EventForm()

    return render(
        request,
        "events/event_form.html",
        {"form": form}
    )

def event_update(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied

    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)

        if form.is_valid():
            form.save()

            return redirect(
                "events:event_detail",
                pk=event.pk
            )
    else:
        form = EventForm(instance=event)

    return render(
        request,
        "events/event_form.html",
        {
            "form": form,
            "event": event,
        }
    )

def event_delete(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied

    event = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        event.delete()
        return redirect("events:event_list")

    return render(
        request,
        "events/event_confirm_delete.html",
        {"event": event},
    )