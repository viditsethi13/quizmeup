# Generated by Django 4.0.3 on 2022-06-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_question_algorithm_question_python'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('algorithm', models.IntegerField()),
                ('database', models.IntegerField()),
                ('java', models.IntegerField()),
                ('python', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='no_of_test',
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='t1',
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='t2',
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='t3',
        ),
        migrations.RemoveField(
            model_name='user_detail',
            name='total_score',
        ),
        migrations.AddField(
            model_name='user_detail',
            name='last_score',
            field=models.IntegerField(default=0),
        ),
    ]
