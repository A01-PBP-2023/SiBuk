from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('merchant_area', models.CharField(blank=True, max_length=255, null=True)),
                ('merchant_name', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(blank=True, choices=[('nasi', 'Nasi'), ('snack', 'Snack'), ('mie', 'Mie'), ('lainnya', 'Lainnya')], max_length=13, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
