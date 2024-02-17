# Generated by Django 4.2.3 on 2024-02-15 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamento', '0002_book_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroVaga', models.CharField(max_length=10, unique=True)),
                ('ocupada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10)),
                ('modelo', models.CharField(default='Desconhecido', max_length=100)),
                ('marca', models.CharField(default='Desconhecido', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Revista',
        ),
        migrations.AddField(
            model_name='patio',
            name='veiculo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacionamento.veiculo'),
        ),
    ]
