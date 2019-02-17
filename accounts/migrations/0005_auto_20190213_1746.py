# Generated by Django 2.1.3 on 2019-02-13 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190213_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password1',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='password2',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
    ]