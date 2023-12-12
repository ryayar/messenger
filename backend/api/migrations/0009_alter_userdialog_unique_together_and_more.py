# Generated by Django 4.2.8 on 2023-12-09 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_sender_userdialog_user1_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userdialog',
            unique_together={('user1', 'user2')},
        ),
        migrations.AlterField(
            model_name='message',
            name='dialog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userdialog'),
        ),
        migrations.RemoveField(
            model_name='userdialog',
            name='dialog',
        ),
        migrations.DeleteModel(
            name='Dialog',
        ),
    ]