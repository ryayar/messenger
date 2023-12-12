from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Добавление дополнительных полей
    phone_number = models.CharField(max_length=15, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)


# class Dialog(models.Model):
#     # Модель для хранения диалогов
#     name = models.CharField(max_length=100)  # Название диалога или любая другая информация о нем


class UserDialog(models.Model):
    # Модель для связи пользователей с диалогами
    # dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)  # Ссылка на диалог
    user1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')  # Отправитель
    user2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')  # Получатель

    class Meta:
        # Уникальный ключ, чтобы каждый диалог имел только двух пользователей
        unique_together = ('user1', 'user2')


class Message(models.Model):
    # Модель для хранения сообщений в чате
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    dialog = models.ForeignKey(UserDialog, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
