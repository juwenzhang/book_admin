# Generated by Django 2.2.12 on 2024-08-19 18:14

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_age', models.IntegerField()),
                ('author_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Author_detailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_address', models.CharField(max_length=100)),
                ('author_email', models.EmailField(max_length=100)),
                ('author_phone', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_name', models.CharField(max_length=100)),
                ('publisher_address', models.CharField(max_length=100)),
                ('publisher_email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('book_publish_date', models.DateField(auto_now_add=True)),
                ('book_author', models.ManyToManyField(to='app01.Author')),
                ('book_publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher')),
            ],
        ),
    ]