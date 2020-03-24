# Generated by Django 2.2.11 on 2020-03-22 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(1, 'In backlog'), (3, 'In progress'), (4, 'Done')])),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.CharField(max_length=10000)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket', to='customerserviceapp.Ticket')),
            ],
        ),
    ]
