# Generated by Django 4.2.3 on 2024-03-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0008_chatbot_rename_info2_user_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='response',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
