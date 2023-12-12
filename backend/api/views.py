from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import uuid

from api.models import CustomUser, UserDialog, Message


class CustomLoginAPIView(APIView):
    def get(self, request):
        return redirect('http://localhost:3000/login/')

    def post(self, request):
        # sender_user = CustomUser.objects.get(username='test')
        # receiver_user = CustomUser.objects.get(username='asdf')
        #
        # # Связываем пользователей с диалогом
        # UserDialog.objects.create(user1=sender_user, user2=receiver_user)
        #
        # # Получаем диалог, к которому будет относиться сообщение (возможно, это диалог между этими пользователями)
        # dialog = UserDialog.objects.get(user1=sender_user)
        #
        # # Создаем и сохраняем сообщение
        # Message.objects.create(
        #     sender=sender_user,
        #     receiver=receiver_user,
        #     dialog=dialog,
        #     content='Привет, как дела?'
        # )

        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = CustomUser.objects.filter(username=username).first()
            if user and user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                if not created:
                    token.delete()
                    token = Token.objects.create(user=user)
                return Response({'type': 'success', 'message': 'Login success', 'token': token.key})
        return Response({'type': 'error', 'message': 'Invalid credentials'})


class RegisterUserAPIView(APIView):
    def get(self, request):
        return redirect('http://localhost:3000/login/')

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            if CustomUser.objects.filter(username=username).exists():
                return Response({'type': 'error', 'message': f'Username \"{username}\" already exists'})
            user = CustomUser.objects.create_user(username=username, password=password)
            return Response({'type': 'success', 'message': f'User \"{user}\" registered successfully'})
        return Response({'type': 'error', 'message': 'Missing username or password'})


class LogoutUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'type': 'success', 'message': 'Logged out successfully'})
        except Token.DoesNotExist:
            return Response({'type': 'error', 'message': 'User token not found'})
        except Exception as e:
            return Response({'type': 'error', 'message': str(e)})


class DialogMessagesAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_messages(self, dialog, user):
        messages = Message.objects.filter(dialog=dialog)
        messages_data = []
        for message in messages:
            message_info = {
                'type': 'out' if message.sender == user else 'in',
                'text': message.content,
                'time': message.timestamp.strftime('%H:%M')
            }
            messages_data.append(message_info)
        return messages_data

    def post(self, request):
        user = request.user  # Получаем текущего пользователя
        user_dialogs = UserDialog.objects.filter(user1=user) | UserDialog.objects.filter(user2=user)

        dialogs_data = []
        for user_dialog in user_dialogs:
            if user == user_dialog.user1 and user == user_dialog.user2:
                dialog_name = 'Заметки'
            elif user == user_dialog.user1:
                dialog_name = user_dialog.user2.username
            else:
                dialog_name = user_dialog.user1.username

            messages_data = self.get_messages(user_dialog.id, user)

            dialog_info = {
                'dialog_id': user_dialog.id,
                'dialog_name': dialog_name,
                'messages': messages_data
            }
            dialogs_data.append(dialog_info)

        return Response(dialogs_data)


class SendMessageAPIView(APIView):
    def post(self, request):
        sender_username = request.data.get('sender')
        dialog_id = request.data.get('dialog_id')
        message_text = request.data.get('message')

        sender_user = get_object_or_404(CustomUser, username=sender_username)
        user_dialog = get_object_or_404(UserDialog, id=dialog_id)

        if sender_user == user_dialog.user2:
            receiver_username = user_dialog.user1.username
        else:
            receiver_username = user_dialog.user2.username

        receiver_user = get_object_or_404(CustomUser, username=receiver_username)

        new_message = Message.objects.create(
            sender=sender_user,
            receiver=receiver_user,
            dialog=user_dialog,
            content=message_text
        )
        new_message.save()

        return Response({'status': 'success', 'message': 'Message sent successfully'})


class SearchUsersAPIView(APIView):
    def post(self, request):
        try:
            sender_user = CustomUser.objects.get(username=request.user)
            receiver_user = CustomUser.objects.get(username=request.data['username']['name'])

            dialog = UserDialog.objects.create(user1=sender_user, user2=receiver_user)

            # Создаем и сохраняем сообщение, используя объект dialog, а не QuerySet
            Message.objects.create(
                sender=sender_user,
                receiver=receiver_user,
                dialog=dialog,
                content='Привет'
            )
        except Exception as err:
            print(err)
        search_text = request.data.get('username')  # Получаем введенный текст из параметра запроса
        if search_text:
            # Ищем пользователей, их имена которых начинаются с введенного текста
            users = CustomUser.objects.filter(username__istartswith=search_text)
            users_list = [
                {'name': user.username, 'code': user.id} for user in users
            ]
            return JsonResponse({'users': users_list}, status=200)
        return JsonResponse({'message': 'Enter a search query'}, status=400)
