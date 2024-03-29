# Generated by Django 5.0.2 on 2024-03-17 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='parent_answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='parent_question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='description',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
