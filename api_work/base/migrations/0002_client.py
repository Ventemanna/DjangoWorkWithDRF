# Generated by Django 5.2 on 2025-05-12 12:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=120)),
                ('client_surname', models.CharField(max_length=120)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский'), ('O', 'Другое')], max_length=1)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.address')),
            ],
        ),
    ]
