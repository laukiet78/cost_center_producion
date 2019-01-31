# Generated by Django 2.1.5 on 2019-01-27 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_quantity'),
        ('manpower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManpowerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(decimal_places=3, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('manpower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manpower.Manpower')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
