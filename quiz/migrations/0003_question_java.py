# Generated by Django 4.0.3 on 2022-03-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_question_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='question_java',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('choice1', models.CharField(max_length=200)),
                ('choice2', models.CharField(max_length=200)),
                ('choice3', models.CharField(max_length=200)),
                ('choice4', models.CharField(max_length=200)),
                ('answer', models.IntegerField()),
            ],
        ),
    ]
