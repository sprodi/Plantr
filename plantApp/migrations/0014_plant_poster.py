# Generated by Django 3.2.3 on 2021-06-10 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_alter_user_id'),
        ('plantApp', '0013_auto_20210610_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='poster',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='login_app.user'),
        ),
    ]
