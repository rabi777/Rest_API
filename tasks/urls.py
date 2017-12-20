from django.conf.urls import url
from tasks.views import *

urlpatterns = [
    url(r'^$', GenerateRandomUserView.as_view(), name='create_user'),
    url(r'^user_list/', ListUser.as_view(), name='user_list'),
]