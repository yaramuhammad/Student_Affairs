# Generated by Django 4.0.4 on 2022-05-18 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_alter_addstudent_mobile_alter_contactus_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstudent',
            name='Department',
            field=models.TextField(choices=[('General', 'General'), ('Bioinformatics', 'Bioinformatics'), ('Data Science', 'Data Science'), ('Cyber Security', 'Cyber Security'), ('Software Engineering', 'Software Engineering'), ('Decision Support', 'Decision Support'), ('Information Technology', 'Information Technology'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Information System', 'Information System'), ('Computer Science', 'Computer Science')], max_length=100),
        ),
    ]
