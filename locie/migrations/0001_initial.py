# Generated by Django 2.2.3 on 2019-08-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('first_name', models.CharField(default='', max_length=30, null=True)),
                ('last_name', models.CharField(default='', max_length=30, null=True)),
                ('phone_number', models.CharField(default='', max_length=30, null=True)),
                ('city', models.CharField(default='', max_length=30, null=True)),
                ('buissness_name', models.CharField(default='', max_length=30, null=True)),
                ('buissness_type', models.CharField(default='', max_length=30, null=True)),
            ],
        ),
    ]
