# Generated by Django 5.0.2 on 2024-02-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0005_alter_member_joineddate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="joineddate",
            field=models.DateField(null=True),
        ),
    ]
