# Generated by Django 3.2.13 on 2022-08-09 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='anonimo', max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('topic', models.CharField(max_length=300, null=True)),
                ('description', models.CharField(blank=True, max_length=2000)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=3000)),
                ('forum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='forumApp.forum')),
            ],
        ),
    ]
