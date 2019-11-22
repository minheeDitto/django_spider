# Generated by Django 2.2.6 on 2019-10-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_filecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='filecontent',
            name='cmd',
            field=models.CharField(default='', max_length=20, verbose_name='运行'),
        ),
        migrations.AddField(
            model_name='filecontent',
            name='display_name',
            field=models.CharField(default='', max_length=20, verbose_name='显示名'),
        ),
        migrations.AddField(
            model_name='filecontent',
            name='file_id',
            field=models.CharField(default='', max_length=30, verbose_name='爬虫id'),
        ),
    ]
