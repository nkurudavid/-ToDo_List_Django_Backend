# Generated by Django 4.2 on 2023-04-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Task Title')),
                ('description', models.TextField(verbose_name='Task Description')),
                ('status', models.CharField(choices=[('todo', 'ToDo'), ('dome', 'Done')], default='todo', max_length=10, verbose_name='Status')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='When Created')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='When Modified')),
            ],
        ),
    ]