# Generated by Django 5.0.2 on 2024-02-22 04:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0006_alter_member_joineddate"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="temp_joineddate",
            field=models.IntegerField(null=True),
        ),
    ]
