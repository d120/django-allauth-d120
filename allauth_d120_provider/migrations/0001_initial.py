# Generated by Django 3.0 on 2019-12-25 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupSync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_group', models.CharField(max_length=100, verbose_name='External group name')),
                ('django_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Django Group')),
            ],
            options={
                'verbose_name': 'Group synchronization',
                'verbose_name_plural': 'Group synchronizations',
            },
        ),
    ]
