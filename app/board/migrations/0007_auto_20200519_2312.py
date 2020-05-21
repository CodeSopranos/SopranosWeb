# Generated by Django 3.0.6 on 2020-05-19 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_dashboard_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='figure',
            name='tag',
        ),
        migrations.AddField(
            model_name='figure',
            name='type',
            field=models.CharField(choices=[('frequency', 'Frequency analysis'), ('wordcloud', 'Wordcloud'), ('correlation', 'Correlation heatmap'), ('sentiment', 'Sentiment analysis')], default='Frequency analysis', max_length=40),
        ),
    ]