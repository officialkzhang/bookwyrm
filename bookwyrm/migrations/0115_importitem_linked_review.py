# Generated by Django 3.2.5 on 2021-11-13 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0114_importjob_source"),
    ]

    operations = [
        migrations.AddField(
            model_name="importitem",
            name="linked_review",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="bookwyrm.review",
            ),
        ),
    ]
