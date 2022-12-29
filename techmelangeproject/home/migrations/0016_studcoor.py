# Generated by Django 4.1.1 on 2022-12-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_festdesc_fest_desc_alter_festdesc_fest_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='studcoor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=122)),
                ('s_desc', models.TextField()),
                ('s_image', models.FileField(default=None, max_length=250, null=True, upload_to='news/')),
                ('s_link', models.URLField()),
            ],
        ),
    ]