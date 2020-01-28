# Generated by Django 3.0.1 on 2020-01-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200128_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='check',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='userinputs',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]