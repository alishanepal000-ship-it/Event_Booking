from django.db import migrations, models
import django.db.models.deletion


def create_default_category(apps, schema_editor):
    Category = apps.get_model("events", "Category")
    Event = apps.get_model("events", "Event")

    category, _ = Category.objects.get_or_create(name="Other")

    Event.objects.filter(category="other").update(category=category.id)


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_event_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        unique=True
                    ),
                ),
            ],
        ),

        migrations.RunPython(
            create_default_category,
            migrations.RunPython.noop,
        ),

        migrations.AlterField(
            model_name="event",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="events",
                to="events.category",
            ),
        ),
    ]