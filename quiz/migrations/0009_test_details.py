# Generated by Django 4.0.3 on 2022-06-21 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_remove_user_detail_test_num_test_number_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('AL', 'algorithm'), ('DB', 'database'), ('JA', 'java'), ('PY', 'python')], default='DB', max_length=2)),
                ('date', models.DateTimeField()),
                ('score', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quiz.user_detail')),
            ],
        ),
    ]
