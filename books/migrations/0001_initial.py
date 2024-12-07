# Generated by Django 5.1.4 on 2024-12-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publication_date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('genre', models.CharField(choices=[('FIC', 'Fiction'), ('NF', 'Non-Fiction'), ('MYST', 'Mystery'), ('SCI', 'Science'), ('FANT', 'Fantasy'), ('BIO', 'Biography'), ('HIST', 'History'), ('ROM', 'Romance'), ('CHILD', 'Children'), ('OTHER', 'Other')], default='OTHER', max_length=10)),
                ('isbn_13', models.CharField(max_length=13, unique=True)),
                ('publisher', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
                ('age_range', models.CharField(choices=[('0-3', '0-3 years'), ('4-7', '4-7 years'), ('8-12', '8-12 years'), ('13-18', '13-18 years'), ('18+', '18+ years')], default='18+', max_length=10)),
            ],
        ),
    ]
