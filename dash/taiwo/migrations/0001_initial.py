# Generated by Django 2.0.3 on 2018-07-28 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taiwo.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('phone_description', models.CharField(max_length=100)),
                ('slug', models.SlugField(default=taiwo.models.generate_id, max_length=10, unique=True)),
                ('video', models.FileField(upload_to=taiwo.models.user_directory_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]