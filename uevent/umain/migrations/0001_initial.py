# Generated by Django 4.0 on 2021-12-26 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Category')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Event text')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Time updated')),
                ('is_published', models.BooleanField(default=True, verbose_name='Is published?')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='umain.category', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Ивент',
                'verbose_name_plural': 'Ивенты',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]
