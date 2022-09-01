# Generated by Django 3.2.14 on 2022-09-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_walking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='walking',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='walking',
            name='date',
            field=models.DateField(verbose_name='walking date'),
        ),
        migrations.AlterField(
            model_name='walking',
            name='schedule',
            field=models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon'), ('N', 'Night')], default='M', max_length=1, verbose_name='walking schedule'),
        ),
        migrations.AddField(
            model_name='dog',
            name='treats',
            field=models.ManyToManyField(to='main_app.Treat'),
        ),
    ]
