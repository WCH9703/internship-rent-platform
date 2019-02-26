# Generated by Django 2.1.7 on 2019-02-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renter_id', models.CharField(max_length=50)),
                ('rentee_id', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1024)),
                ('post_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renter_id', models.CharField(max_length=50)),
                ('rentee_id', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1024)),
                ('create_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('room_id', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1024)),
                ('post_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('room_id', models.CharField(max_length=50)),
                ('create_time', models.DateField()),
                ('rent_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('rent_amount', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=20)),
                ('longtitude', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('is_co_rent', models.CharField(max_length=20)),
                ('detail', models.CharField(max_length=255)),
                ('rank', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=20)),
                ('passwd', models.CharField(max_length=20)),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('identify_code', models.CharField(max_length=20)),
                ('utype', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=255)),
            ],
        ),
    ]