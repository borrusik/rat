# Generated by Django 5.1.5 on 2025-02-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback_app', '0002_alter_feedback_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='professors_photos/'),
        ),
    ]
