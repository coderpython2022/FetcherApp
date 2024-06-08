# Generated by Django 4.2.10 on 2024-06-08 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facebook', '0005_accountinfo_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=1, max_length=100, null=1)),
                ('password', models.CharField(blank=1, max_length=100, null=1)),
                ('created', models.DateTimeField(auto_now_add=True, null=1)),
            ],
        ),
    ]