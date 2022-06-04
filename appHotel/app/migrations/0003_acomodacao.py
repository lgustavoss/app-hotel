# Generated by Django 4.0.4 on 2022-06-01 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tiposacomodacao_alter_cliente_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acomodacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidade', models.IntegerField(max_length=3, unique=True)),
                ('andar', models.IntegerField(blank=True, max_length=2, null=True)),
                ('ramal', models.CharField(blank=True, max_length=10, unique=True)),
                ('capacidade', models.IntegerField(max_length=2, null=True)),
                ('valor', models.FloatField()),
                ('status', models.CharField(choices=[('Ocupado', 'Ocupado'), ('Desativado', 'Desativado'), ('Livre', 'Livre'), ('Em manutenção', 'Em manutenção')], max_length=15)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tiposacomodacao', unique=True)),
            ],
        ),
    ]