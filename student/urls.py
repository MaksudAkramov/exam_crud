from django.urls import path
from rest_framework_simplejwt import views as jwt_views


from rest_framework.routers import SimpleRouter
from student import views
from rest_framework_simplejwt.views import TokenVerifyView

router = SimpleRouter()
router.register('', views.AccountViewSet)


urlpatterns=[
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]+ router.get_urls()