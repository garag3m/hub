from django.urls import path

from rest_framework import routers

app_name = 'core'

router = routers.DefaultRouter()

# router.register(r'user', views.UUIDUserViewSet, base_name='api-user')
# router.register(r'environments', views.EnvironmentViewSet, base_name='api-environments')
# router.register(r'scenes', views.SceneViewSet, base_name='api-scenes')
# router.register(r'devices', views.DeviceViewSet, base_name='api-devices')
# router.register(r'history', views.HistoryViewSet, base_name='api-history')
# router.register(r'commands', views.CommandViewSet, base_name='api-commands')
# router.register(r'schedulings', views.SchedulingViewSet, base_name='api-schedulings')
# router.register(r'exceptions', views.SchedulingExceptionViewSet, base_name='api-exceptions')

# urlpatterns = router.urls

# urlpatterns += [
#     # Auth
#     path('auth/', views.AuthToken.as_view()),
# ]