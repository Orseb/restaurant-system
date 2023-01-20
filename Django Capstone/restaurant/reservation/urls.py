from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView, msg
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('message/', msg),
    path('api-token-auth/', obtain_auth_token),
]