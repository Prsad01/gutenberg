# Generated by Django 4.2.11 on 2024-03-19 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('birth_year', models.SmallIntegerField(blank=True, null=True)),
                ('death_year', models.SmallIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('download_count', models.IntegerField(blank=True, null=True)),
                ('gutenberg_id', models.IntegerField(unique=True)),
                ('media_type', models.CharField(max_length=16)),
                ('title', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mime_type', models.CharField(max_length=32)),
                ('url', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookSubjects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.subject')),
            ],
        ),
        migrations.CreateModel(
            name='BookLanguages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.language')),
            ],
        ),
        migrations.CreateModel(
            name='BookBookshelves',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('bookshelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookshelf')),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
    ]