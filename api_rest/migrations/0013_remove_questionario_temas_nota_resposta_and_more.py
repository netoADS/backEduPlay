# Generated by Django 5.0.4 on 2024-05-14 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0012_aluno_professor_questionario_nota_tema_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario',
            name='temas',
        ),
        migrations.AddField(
            model_name='nota',
            name='resposta',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='questionario',
            name='tema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionarios', to='api_rest.tema'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='api_rest.aluno'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='nota',
            name='questionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='api_rest.questionario'),
        ),
    ]