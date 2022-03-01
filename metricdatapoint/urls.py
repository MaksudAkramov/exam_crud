from rest_framework.routers import SimpleRouter
from metricdatapoint import views
router = SimpleRouter()
router.register('', views.MatricDataViewset)


urlpatterns=[

]+ router.get_urls()