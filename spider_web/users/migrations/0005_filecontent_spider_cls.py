# Generated by Django 2.2.7 on 2019-11-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191029_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='filecontent',
            name='spider_cls',
            field=models.CharField(default='', max_length=20, verbose_name='爬虫类'),
        ),
    ]
