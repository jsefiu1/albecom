# Generated by Django 5.0.2 on 2024-02-14 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]
