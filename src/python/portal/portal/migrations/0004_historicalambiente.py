# Generated by Django 4.1.3 on 2022-12-13 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0003_alter_ambiente_cor_alter_ambiente_sigla'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAmbiente',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('sigla', models.CharField(db_index=True, help_text='Esta é a sigla que vai aparecer no dashboard', max_length=255, verbose_name='sigla do ambiente')),
                ('cor', models.CharField(help_text="Escolha uma cor em RGB. Ex.: <span style='background: #a154d0; color: #fff; padding: 1px 5px; font-size: 95%; border-radius: 4px;'>#a154d0</span> <span style='background: #438f4b; color: #fff; padding: 1px 5px; font-size: 95%; border-radius: 4px;'>#438f4b</span> <span style='background: #c90c0f; color: #fff; padding: 1px 5px; font-size: 95%; border-radius: 4px;'>#c90c0f</span>", max_length=255, verbose_name='cor do ambiente')),
                ('nome', models.CharField(max_length=255, verbose_name='nome do ambiente')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('token', models.CharField(max_length=255, verbose_name='token')),
                ('active', models.BooleanField(default=True, verbose_name='ativo?')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ambiente',
                'verbose_name_plural': 'historical ambientes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
