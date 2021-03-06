# Generated by Django 2.1.5 on 2019-01-12 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad', models.CharField(max_length=255, verbose_name='Entidad')),
                ('fuente', models.URLField(max_length=255, verbose_name='fuente')),
                ('estatus', models.SmallIntegerField(choices=[(1, 'Nuevo'), (2, 'Plan requiere documento para su revisión'), (3, 'Documento requiere revisión'), (4, 'Documento en revisión'), (5, 'Documento ha sido revisado')], default=1, verbose_name='Estatus')),
                ('documento', models.FileField(blank=True, upload_to='files', verbose_name='Documento')),
                ('publicado', models.DateField(verbose_name='Fecha de publicación')),
                ('revisado', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de revisión')),
                ('comentarios', models.TextField(blank=True, null=True, verbose_name='Comentarios de la revisión')),
                ('revisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='planes', to=settings.AUTH_USER_MODEL, verbose_name='Revisor')),
            ],
            options={
                'verbose_name': 'Plan de Implementación',
                'verbose_name_plural': 'Planes de Implementación',
                'ordering': ['-publicado'],
                'get_latest_by': 'publicado',
            },
        ),
    ]
