from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from student import views
from rest_framework_simplejwt.views import TokenVerifyView



urlpatterns=[
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('create/', views.add_car, name='add-car'),
    path('all/', views.view_car, name='view_car'),
    path('update/<int:pk>/', views.update_car, name='update-car'),
]