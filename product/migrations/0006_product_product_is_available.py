# Generated by Django 4.2.3 on 2023-10-01 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_review_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_is_available',
            field=models.BooleanField(default=True),
        ),
    ]
