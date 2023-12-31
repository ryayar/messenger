# Generated by Django 4.2.8 on 2023-12-08 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_userdialog_unique_together_userdialog_receiver_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdialog',
            old_name='sender',
            new_name='user1',
        ),
        migrations.RenameField(
            model_name='userdialog',
            old_name='receiver',
            new_name='user2',
        ),
        migrations.AlterUniqueTogether(
            name='userdialog',
            unique_together={('dialog', 'user1', 'user2')},
        ),
    ]
