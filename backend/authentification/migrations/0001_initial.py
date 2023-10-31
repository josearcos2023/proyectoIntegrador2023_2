# Generated by Django 4.2.6 on 2023-10-31 04:30

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
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('condicion', models.CharField(max_length=50)),
                ('fecha', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='static/img/')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(max_length=50)),
                ('es_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id_transaccion', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_transaccion', models.DateField(auto_now=True)),
                ('precio_transaccion', models.FloatField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('completada', 'Completada'), ('cancelada', 'Cancelada')], max_length=20)),
                ('id_comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compra', to='authentification.users')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.producto')),
                ('id_vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta', to='authentification.users')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.users'),
        ),
    ]
