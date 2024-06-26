# Generated by Django 5.0 on 2024-03-14 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_work', '0002_usergarbagebin_status_alter_usergarbagebin_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='collectionstatus',
            name='collectonrequest',
        ),
        migrations.RemoveField(
            model_name='garbagebin',
            name='assigned',
        ),
        migrations.CreateModel(
            name='CollectionMessege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_work.area')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_work.garbagebin')),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('buildingno', models.CharField(max_length=100)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='my_work.area')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='CollectionRequest',
        ),
        migrations.DeleteModel(
            name='CollectionStatus',
        ),
    ]
