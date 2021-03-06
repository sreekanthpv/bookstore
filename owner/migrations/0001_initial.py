# Generated by Django 3.2.6 on 2021-09-06 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=100, unique=True)),
                ('author', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('copies', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('delivered', 'delivered'), ('intransit', 'intransit'), ('ordered', 'ordered'), ('cancelled', 'cancelled')], default='ordered', max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('expected_delivery_date', models.DateField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.book')),
            ],
        ),
    ]
