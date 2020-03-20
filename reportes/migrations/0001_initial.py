# Generated by Django 3.0.4 on 2020-03-19 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('type_id', models.IntegerField()),
                ('uuid', models.CharField(max_length=255)),
                ('receiver', models.CharField(max_length=255)),
                ('xml', models.TextField()),
                ('metadato', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]