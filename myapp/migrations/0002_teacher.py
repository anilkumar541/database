# Generated by Django 3.2.9 on 2021-12-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=88)),
                ('student', models.ManyToManyField(to='myapp.Student')),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]