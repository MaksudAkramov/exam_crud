from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from student import views
from rest_framework_simplejwt.views import TokenVerifyView



urlpatterns=[
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('create/', views.add_student, name='add-student'),
    path('all/', views.view_student, name='view_student'),
    path('update/<int:pk>/', views.update_student, name='update-student'),
]