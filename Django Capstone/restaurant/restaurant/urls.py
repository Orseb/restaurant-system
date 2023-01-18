from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservation import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reservation.urls')),
    path('api/book/', include(router.urls))
]
