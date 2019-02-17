# Generated by Django 2.1.3 on 2019-02-13 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190212_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='fullname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_photo',
            field=models.ImageField(upload_to='', verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
        ),
    ]
