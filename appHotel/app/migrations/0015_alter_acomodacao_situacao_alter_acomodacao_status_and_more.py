# Generated by Django 4.0.4 on 2022-06-04 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_acomodacao_situacao_alter_acomodacao_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acomodacao',
            name='situacao',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='acomodacao',
            name='status',
            field=models.CharField(choices=[('Livre', 'Livre'), ('Ocupado', 'Ocupado'), ('Em manutenção', 'Em manutenção'), ('Reservado', 'Reservado')], max_length=15),
        ),
        migrations.AlterField(
            model_name='acomodacao',
            name='unidade',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
