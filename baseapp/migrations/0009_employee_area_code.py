# Generated by Django 3.1.5 on 2021-04-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0008_auto_20210407_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='area_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]