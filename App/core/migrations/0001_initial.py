# Generated by Django 4.0.1 on 2022-06-08 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de categoría')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('producto', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Producto')),
                ('flor', models.CharField(max_length=20, verbose_name='Tipo de flor')),
                ('fertilizador', models.CharField(max_length=20, verbose_name='Tipo fertilizador')),
                ('arbusto', models.CharField(max_length=20, verbose_name='Tipo arbusto')),
                ('maceta', models.CharField(max_length=20, verbose_name='Tamaño maceta')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
