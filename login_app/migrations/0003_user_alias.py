# Generated by Django 3.2.3 on 2021-06-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(default='Sean', max_length=50),
            preserve_default=False,
        ),
    ]
