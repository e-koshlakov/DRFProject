from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserObtainTokenView

app_name = UsersConfig.name

urlpatterns = [
    # users urlpatterns
    path('', UserListAPIView.as_view(), name='users_list'),
    path('create/', never_cache(UserCreateAPIView.as_view()), name='user_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', never_cache(UserUpdateAPIView.as_view()), name='user_update'),
    path('delete/<int:pk>/', never_cache(UserDestroyAPIView.as_view()), name='user_delete'),
    # token urlpatterns
    path('token/', never_cache(UserObtainTokenView.as_view()), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
