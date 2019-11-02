# Generated by Django 2.2.5 on 2019-11-02 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('team_group_numbers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teams.Teams')),
            ],
        ),
    ]
