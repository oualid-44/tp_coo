# Generated by Django 4.2.16 on 2024-09-26 12:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("high_level", "0002_alter_etape_etape_suivante_alter_etape_machine_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stock",
            old_name="objet",
            new_name="ressource",
        ),
    ]
