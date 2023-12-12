from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
# from .views import RegisterUserAPIView, LogoutUserAPIView, CustomLoginAPIView, UserDialogsAPIView

urlpatterns = [
    path('token/', obtain_auth_token, name='get_auth_token'),  # Получение токена
    path('login/', CustomLoginAPIView.as_view(), name='custom_login'),  # Вход пользователя (логин)
    path('register/', RegisterUserAPIView.as_view(), name='register_user'),  # Регистрация пользователя
    path('logout/', LogoutUserAPIView.as_view(), name='logout_user'),  # Выход пользователя
    path('get_dialogs/', DialogMessagesAPIView.as_view(), name='get_dialogs'),  # Выход пользователя
    # path('get_dialogs/', UserDialogsAPIView.as_view(), name='get_dialogs'),  # Выход пользователя
    path('send/', SendMessageAPIView.as_view(), name='send_message'),  # Выход пользователя
    path('search/', SearchUsersAPIView.as_view(), name='search_users'),  # Выход пользователя
    # path('logout/', knox_views.as_view(), name='logout_user'),  # Выход пользователя
    # Другие URL-маршруты вашего приложения
]
