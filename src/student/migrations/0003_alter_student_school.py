# Generated by Django 4.0.4 on 2022-05-11 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('src_school', '0001_initial'),
        ('src_student', '0002_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_id', to='src_school.school'),
        ),
    ]