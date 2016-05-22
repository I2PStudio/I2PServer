import logging
import os

from qiniu import Auth
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from upload.models import File

logger = logging.getLogger(__name__)

access_key = os.environ['QINIU_ACCESS_KEY']
secret_key = os.environ['QINIU_SECRET_KEY']
bucket_name = 'i2pserver'
base_url = 'o7f53wsde.bkt.clouddn.com'

policy = {
    'callbackUrl': 'http://api.joway.wang/upload/callback/',
    'callbackBody': 'filename=$(fname)&filesize=$(fsize)&type=$(mimeType)&hash=$(etag)'
}
q = Auth(access_key, secret_key)


# 七牛云存储支持
class UploadViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = File.objects.all()

    @list_route(methods=['post'])
    def token(self, request, *args, **kwargs):
        """
        Get open problem detail
        """
        token = q.upload_token(bucket_name, None, 7200, policy)
        return Response({"token": token})

    @list_route(methods=['post', 'get'], permission_classes=[AllowAny, ])
    def callback(self, request, *args, **kwargs):
        """
        Get open problem detail
        """
        info = {
            'filename': request.POST.get('filename'),
            'filesize': request.POST.get('filesize'),
            'type': request.POST.get('type'),
            'hash': request.POST.get('hash'),
        }
        logger.info(info)
        File.objects.create(url=base_url + info['filename'],
                            mime_type=info['type'], hash=info['hash'])
        return Response({"message": "callback success"})

    @list_route(methods=['get'])
    def data(self, request, *args, **kwargs):
        return Response(self.get_queryset())
