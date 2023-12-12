import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async

from api.models import *


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.auth_token = self.scope['cookies'].get('token')  # Пример получения токена из query_string
        self.user = await self.get_user_by_token(self.auth_token)
        if not self.user or isinstance(self.user, AnonymousUser):
            await self.close()
        else:
            self.room_name = f"user_{self.user.id}"
            await self.channel_layer.group_add(
                self.room_name,
                self.channel_name
            )

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sender = self.user
        message = text_data_json['message']
        dialog_id = text_data_json['dialog_id']

        await self.save_message(sender, message, dialog_id)
        get_new_message = await self.get_message(sender, dialog_id)
        if not sender == self.receiver_user:
            await self.channel_layer.group_send(
                f"user_{self.receiver_user.id}",  # Название комнаты, в которую вы хотите отправить сообщение
                {
                    "type": "chat.message",  # Название метода в consumer'е, который будет обрабатывать это сообщение
                    "data": json.dumps({
                        'data': get_new_message
                    }),
                },
            )

    async def chat_message(self, event):
        data = event["data"]
        await self.send(text_data=data)

    @database_sync_to_async
    def get_user_by_token(self, token):
        try:
            return Token.objects.get(key=token).user
        except Token.DoesNotExist:
            return None

    @database_sync_to_async
    def save_message(self, sender_username, message_text, dialog_id):
        sender_user = CustomUser.objects.get(username=sender_username)
        user_dialog = UserDialog.objects.get(id=dialog_id)

        if sender_user == user_dialog.user2:
            receiver_username = user_dialog.user1.username
        else:
            receiver_username = user_dialog.user2.username

        self.receiver_user = CustomUser.objects.get(username=receiver_username)

        new_message = Message.objects.create(
            sender=sender_user,
            receiver=self.receiver_user,
            dialog=user_dialog,
            content=message_text
        )
        new_message.save()

    @database_sync_to_async
    def get_message(self, sender_username, dialog_id):
        message = Message.objects.filter(dialog=dialog_id).order_by('-id').first()
        message_info = {
            'type': 'in' if message.sender == sender_username else 'out',
            'text': message.content,
            'time': message.timestamp.strftime('%H:%M'),
            'dialog_id': message.dialog_id
        }
        return message_info

