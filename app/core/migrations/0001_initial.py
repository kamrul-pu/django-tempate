# Generated by Django 5.0 on 2024-01-23 14:24

import autoslug.fields
import core.utils
import uuid
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=150)),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=150)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='first_name', unique=True)),
                ('gender', models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('UNKNOWN', 'Unknown'), ('OTHER', 'Other')], default='UNKNOWN', max_length=20)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, upload_to=core.utils.get_user_media_path_prefix, verbose_name='Profile_image')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('kind', models.CharField(choices=[('ADMIN', 'Admin'), ('DEVELOPER', 'Developer'), ('SUPER_ADMIN', 'Super Admin'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'System User',
                'verbose_name_plural': 'System Users',
            },
        ),
    ]
