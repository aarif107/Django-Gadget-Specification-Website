# Generated by Django 3.1 on 2020-08-23 17:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]