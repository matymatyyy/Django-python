# Generated by Django 4.2.5 on 2023-10-10 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrito', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gmail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.AddField(
            model_name='compra',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.usuario'),
        ),
    ]
