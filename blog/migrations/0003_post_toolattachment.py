# Generated by Django 4.2 on 2023-11-14 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
        ('blog', '0002_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='toolattachment',
            field=models.ForeignKey(blank=True, help_text="Select a tool's function to display in post_details.html", null=True, on_delete=django.db.models.deletion.SET_NULL, to='converter.toolattachment'),
        ),
    ]
