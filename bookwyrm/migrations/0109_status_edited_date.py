# Generated by Django 3.2.5 on 2021-10-15 15:54

import bookwyrm.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0108_alter_user_preferred_language"),
    ]

    operations = [
        migrations.AddField(
            model_name="status",
            name="edited_date",
            field=bookwyrm.models.fields.DateTimeField(blank=True, null=True),
        ),
    ]