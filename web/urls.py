from django.conf.urls import url
from web.views import *

urlpatterns = [
    url(r'^rest-api', webApiView.as_view(), name='web'),
    url(r'^create-student', RestApi.as_view(), name='create-web-rest'),
]