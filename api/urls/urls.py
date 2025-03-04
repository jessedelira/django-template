from rest_framework import routers

from api.controllers import DogController

router = routers.DefaultRouter()
router.register(r"dogs", DogController)

urlpatterns = router.urls
