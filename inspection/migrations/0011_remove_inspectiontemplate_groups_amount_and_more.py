# Generated by Django 4.2.13 on 2024-06-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0010_remove_inspectionitem_group_inspectiongroup_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspectiontemplate',
            name='groups_amount',
        ),
        migrations.AlterField(
            model_name='inspectiongroup',
            name='group',
            field=models.CharField(choices=[('piv', 'piv'), ('reparos_estruturais', 'reparos_estruturais'), ('vis_vidros', 'vis_vidros'), ('registro_km', 'registro_km'), ('grupo_extra', 'grupo_extra')], max_length=255, verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='inspectiongroup',
            name='items',
            field=models.ManyToManyField(related_name='group', to='inspection.inspectionitem', verbose_name='Itens'),
        ),
        migrations.AlterField(
            model_name='inspectiontemplate',
            name='inspection_groups',
            field=models.ManyToManyField(related_name='templates', to='inspection.inspectiongroup', verbose_name='Grupos'),
        ),
    ]
