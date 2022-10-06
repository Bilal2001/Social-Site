from django.urls import path
from .views import GroupList, GroupCreate, GroupDetail, GroupJoin, GroupLeave
app_name = 'groups'
urlpatterns = [
    path('', GroupList.as_view(), name = "list"),
    path('in/<slug>/', GroupDetail.as_view(), name = "detail"),
    path('create/', GroupCreate.as_view(), name = "create"),
    path('join/<slug>/', GroupJoin.as_view(), name = "join"),
    path('leave/<slug>/', GroupLeave.as_view(), name = "leave"),
]