# Generated by Django 3.2.6 on 2021-09-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_authors_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notas',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]