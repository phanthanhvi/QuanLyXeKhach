# Generated by Django 3.2.6 on 2021-08-12 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghe',
            name='soXe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Ghe_soXe', to='quanly.loaixe'),
        ),
    ]