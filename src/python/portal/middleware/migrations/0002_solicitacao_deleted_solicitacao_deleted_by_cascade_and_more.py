# Generated by Django 4.1.4 on 2022-12-13 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_ambiente_deleted_ambiente_deleted_by_cascade_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('middleware', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='deleted',
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='deleted_by_cascade',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.CreateModel(
            name='HistoricalSolicitacao',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('timestamp', models.DateTimeField(blank=True, editable=False, verbose_name='quando ocorreu')),
                ('requisicao', models.TextField(blank=True, null=True, verbose_name='requisição')),
                ('requisicao_header', models.JSONField(blank=True, null=True, verbose_name='cabeçalho da requisição')),
                ('resposta', models.TextField(blank=True, null=True, verbose_name='resposta')),
                ('resposta_header', models.JSONField(blank=True, null=True, verbose_name='cabeçalho da resposta')),
                ('status', models.CharField(blank=True, choices=[('S', 'Sucesso'), ('F', 'Falha')], max_length=256, null=True, verbose_name='status')),
                ('status_code', models.CharField(blank=True, max_length=256, null=True, verbose_name='status code')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('campus', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='portal.campus')),
                ('diario', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='portal.diario')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical solicitação',
                'verbose_name_plural': 'historical solicitações',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
