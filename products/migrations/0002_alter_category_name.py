# Generated by Django 4.2 on 2023-04-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Analgesics/Pain Relievers", "Analgesics/Pain Relievers"),
                    ("Antibiotics", "Antibiotics"),
                    ("Antidepressants", "Antidepressants"),
                    ("Antihistamines", "Antihistamines"),
                    ("Antihypertensives", "Antihypertensives"),
                    ("Anti-inflammatory Drugs", "Anti-inflammatory Drugs"),
                    ("Antacids", "Antacids"),
                    ("Anticoagulants", "Anticoagulants"),
                    ("Asthma Medications", "Asthma Medications"),
                    ("Diabetes Medications", "Diabetes Medications"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]