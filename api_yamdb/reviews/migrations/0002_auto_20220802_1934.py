# Generated by Django 2.2.16 on 2022-08-02 19:34

import django.db.models.deletion
from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='unique_titles_author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='titles',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='title',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='title', to='reviews.Category'),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('title', 'author'), name='unique_titles_author'),
        ),
    ]
