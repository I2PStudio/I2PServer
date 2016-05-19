from rest_framework import routers

from upload.apis import UploadViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r"upload", UploadViewSet, base_name="upload")
