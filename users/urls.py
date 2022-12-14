from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users import views

urlpatterns = [
    path('signup/', views.UserView.as_view(), name='signup'),
    path('mock/', views.MockView.as_view(), name='mock'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
