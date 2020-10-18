# Generated by Django 3.1.2 on 2020-10-18 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BookingModel",
            fields=[
                ("booking_id", models.UUIDField(primary_key=True, serialize=False)),
                ("user_id", models.UUIDField()),
                ("vehicle_model_id", models.IntegerField()),
                ("package_id", models.CharField(max_length=2)),
                ("travel_type_id", models.CharField(max_length=2)),
                ("from_area_id", models.IntegerField()),
                ("to_area_id", models.IntegerField()),
                ("from_city_id", models.IntegerField()),
                ("to_city_id", models.IntegerField()),
                ("from_date", models.DateTimeField()),
                ("to_date", models.DateTimeField()),
                ("online_booking", models.BooleanField()),
                ("mobile_site_booking", models.BooleanField()),
                ("booking_created", models.DateTimeField()),
                ("from_lat", models.DecimalField(decimal_places=5, max_digits=8)),
                ("from_long", models.DecimalField(decimal_places=5, max_digits=8)),
                ("to_lat", models.DecimalField(decimal_places=5, max_digits=8)),
                ("to_long", models.DecimalField(decimal_places=5, max_digits=8)),
                ("car_cancellation", models.BooleanField()),
            ],
        )
    ]
