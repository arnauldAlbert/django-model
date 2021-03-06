# Generated by Django 4.0.3 on 2022-04-03 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='livre',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.categorie'),
        ),
    ]
