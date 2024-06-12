# Generated by Django 4.2 on 2024-06-12 06:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0002_rename_chat_conversation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="conversation",
            name="chat_history",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(), default=list, size=None
            ),
        ),
    ]