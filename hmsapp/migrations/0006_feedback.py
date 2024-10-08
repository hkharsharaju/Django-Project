# Generated by Django 3.0 on 2023-08-11 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0005_auto_20230810_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fdtp', models.CharField(choices=[('0', '---Select Staff Type---'), ('Receptionist', 'Receptionist'), ('House Keeping', 'House Keeping'), ('Porter', 'Porter'), ('Restaurant Staff', 'Restaurant Staff')], default='0', max_length=20)),
                ('fd', models.CharField(max_length=200)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
