# Generated by Django 4.1.11 on 2023-09-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapapi', '0002_alter_scrapa_transcript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapa',
            name='channel_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scrapa',
            name='channel_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scrapa',
            name='sentiment',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scrapa',
            name='title',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='scrapa',
            name='video_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]