# Generated by Django 4.0.5 on 2022-06-12 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HildaApp', '0004_rename_nombre_producto_producto_nombreproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='image',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
